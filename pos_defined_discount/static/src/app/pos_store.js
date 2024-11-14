/** @odoo-module **/

import { PosStore } from "@point_of_sale/app/store/pos_store";
import { patch } from "@web/core/utils/patch";

patch(PosStore.prototype, {
    async _processData(loaderData)
    {
        await super._processData(...arguments);
        this.discount = loaderData["pos.custom.discount"]
    }
});