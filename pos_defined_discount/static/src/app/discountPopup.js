/** @odoo-module */

import { AbstractAwaitablePopup } from "@point_of_sale/app/popup/abstract_awaitable_popup";
import { _t } from "@web/core/l10n/translation";
import { useState, useRef } from "@odoo/owl";

export class DiscountPopup extends AbstractAwaitablePopup {
    static template = "pos_defined_discount.DiscountPopup";
    static defaultProps = {
        confirmText: _t("Apply Discount"),
        cancelText: _t("Cancel"),
        removeText: _t("Remove Discount"),
        title: _t("Select"),
        body: "",
        startingValue: 0,
        list: [],
        confirmKey: true,
        placeholder: "Choose Discount",
        wholeOrder: false,
        onlyLine: false,
        customDiscount: false,
    };

    /**
     * Value of the `item` key of the selected element in the Selection
     * Array is the payload of this popup.
     *
     * @param {Object} props
     * @param {String} [props.confirmText='Confirm']
     * @param {String} [props.cancelText='Cancel']
     * @param {String} [props.title='Select']
     * @param {String} [props.body='']
     * @param {Array<Selection>} [props.list=[]]
     *      Selection {
     *          id: integer,
     *          label: string,
     *          isSelected: boolean,
     *          item: any,
     *      }
     */
    setup() 
    {
        super.setup();
        this.state = useState({ selectedId: this.props.list.find((item) => item.isSelected), inputValue: this.props.startingValue, wholeOrder: this.props.wholeOrder, onlyLine: this.props.onlyLine});
        this.inputRef = useRef("input", "checkbox");
    }
    selectItem(itemId) 
    {
        this.state.selectedId = itemId;
        this.confirm();
    }
    remove()
    {
        this.state.selectedId = 0;
        this.confirm();
    }
    checkWhole()
    {
        this.state.wholeOrder = true;
        this.state.onlyLine = false;
    }
    checkLiner()
    {
        this.state.onlyLine = true;
        this.state.wholeOrder = false;
    }
    /**
     * We send as payload of the response the selected item.
     *
     * @override
     */
    getPayload() 
    {
        const selected = this.props.list.find((item) => this.state.selectedId === item.id);
        if(selected && selected.item)
        {
            return [selected && selected.item, this.state.wholeOrder, this.state.onlyLine];
        }
        else if(this.state.startingValue)
        {
            return [this.state.startingValue.replace(/[^0-9]/g, '').trim(), this.state.wholeOrder, this.state.onlyLine];
        }
        else
        {
            return [selected && selected.item, this.state.wholeOrder, this.state.onlyLine];
        } 
    }
}
