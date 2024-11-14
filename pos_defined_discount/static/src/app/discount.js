/** @odoo-module **/

import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { DiscountPopup } from "@pos_defined_discount/app/discountPopup";
import { ConfirmPopup } from "@point_of_sale/app/utils/confirm_popup/confirm_popup";
import { patch } from "@web/core/utils/patch";

patch(ProductScreen.prototype, {
    getDiscount()
    {
        let discount = [];
        let discounts = this.env.services.pos.discount;
        for(let get_discounts in discounts)
        {
            discount.push({
                id: discounts[get_discounts]['id'],
                label: discounts[get_discounts]['custom_discount_name'],
                item: discounts[get_discounts]['custom_percentage'],
            });    
        }
        return discount;
    },
    async getUserDiscount()
    {
        let order = this.env.services.pos.get_order();
        try
        {
            const res = await this.env.services.orm.silent.call(
                'pos.config',
                'get_discount_group',
                [this.env.services.pos.config.id]
            );
            order.customDiscount = res;
        }
        catch(error)
        {
            console.error(error);
        }
    },
    /*async onNumpadClick(buttonValue)
    {
        if(["discount"].includes(buttonValue))
        {
            this.numberBuffer.capture();
            this.numberBuffer.reset();
            this.pos.numpadMode = false;
            await this.getUserDiscount();
            this.click();
            return;
        }
        this.numberBuffer.sendKey(buttonValue);
    },*/

    async onNumpadClick(buttonValue) {
        if (["quantity", "discount", "price"].includes(buttonValue)) {
            this.numberBuffer.capture();
            this.numberBuffer.reset();
            if (buttonValue=='discount'){
                await this.getUserDiscount();
                this.click();
            }
            this.pos.numpadMode = buttonValue;
            return;
        }
        this.numberBuffer.sendKey(buttonValue);
    },
    async click()
    {
        let orderline =  this.currentOrder.get_orderlines();
        let order = this.env.services.pos.get_order();
        if(this.currentOrder.orderlines.length == 0)
        {
            const { confirmed } = await this.popup.add(ConfirmPopup, {
                title: "Error",
                body: "Can't apply discounts to an empty order."
            });
            return;
        }
        if(this.getDiscount().length == 0)
        {
            const { confirmed } = await this.popup.add(ConfirmPopup, {
                title: "Error",
                body: "No predifined discount where found."
            });
            return;
        }
        else
        {
            const { confirmed, payload: discounts } = await this.popup.add(DiscountPopup, {
                title: "Choose Discount",
                list: this.getDiscount(),
                wholeOrder: order.wholeOrder,
                onlyLine: order.onlyLine
            });
            if(confirmed)
            {
                if(discounts[1] == false && discounts[2] == false)
                {
                    this.numberBuffer.reset();
                    this.pos.numpadMode = "discount";
                    this._setValue(discounts[0]);
                    this.pos.numpadMode = "quantity";
                    order.wholeOrder = discounts[1];
                    order.onlyLine = discounts[2];
                    return true;
                }
                else if(discounts[1] == true)
                {
                    this.numberBuffer.reset();
                    this.pos.numpadMode = "discount";
                    for (let orderlines in orderline)
                    {
                        orderline[orderlines].set_discount(discounts[0]);
                    }
                    this.pos.numpadMode = "quantity";
                    order.wholeOrder = discounts[1];
                    order.onlyLine = discounts[2];
                    return true;
                }
                else
                {
                    this.numberBuffer.reset();
                    this.pos.numpadMode = "discount";
                    this._setValue(discounts[0]);
                    this.pos.numpadMode = "quantity";
                    order.wholeOrder = discounts[1];
                    order.onlyLine = discounts[2];
                    return true;
                }
            }
            else
            {
                this.pos.numpadMode = "quantity";
            }
        }
    }
});