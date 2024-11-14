/** @odoo-module */

import { Order } from "@point_of_sale/app/store/models";
import { patch } from "@web/core/utils/patch";

patch(Order.prototype, 
{
    //@override
    export_as_JSON() 
    {
        const json = super.export_as_JSON(...arguments);
        json.wholeOrder = this.wholeOrder;
        json.onlyLine = this.onlyLine;
        json.customDiscount = this.customDiscount;
        return json;
    },

    //@override
    init_from_JSON(json) 
    {
        super.init_from_JSON(...arguments);
        this.wholeOrder = json.wholeOrder;
        this.onlyLine = json.onlyLine;
        this.customDiscount = json.customDiscount;
    },
});