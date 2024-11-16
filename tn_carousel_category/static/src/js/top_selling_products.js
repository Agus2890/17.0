/** @odoo-module **/
import publicWidget from "@web/legacy/js/public/public_widget";
import { jsonrpc } from "@web/core/network/rpc_service";
import { registry } from '@web/core/registry';
import { renderToElement } from "@web/core/utils/render";
import { onWillStart } from "@odoo/owl";
     /**
     * Widget for displaying top-selling products in categories.
     */
publicWidget.registry.TopSellingProducts = publicWidget.Widget.extend({
        selector: '.products_category_wise_snippet',
        /**
         * Load products and categories data from the server.
         */
   init() {
        this._super(...arguments);
        this.rpc = this.bindService("rpc");
    },
        /**
         * Render the widget with the fetched data.
         */
        start: async function() {

            await this.rpc('/category_ecomerce_product', {}).then((data) => {
                this.data = data;
            })

            function getChunkSize() {
                // Comprobamos el tamaño de la pantalla para definir cuántos elementos mostrar
                if (window.innerWidth <= 768) {
                    // Si el ancho es menor o igual a 768px (dispositivos móviles y tablets)
                    return 4;
                } else {
                    // Si es mayor que 768px (pantallas grandes)
                    return 6;
                }
            }

            function chunkArray(arr, size) {
              const result = [];
              for (let i = 0; i < arr.length; i += size) {
                result.push(arr.slice(i, i + size));
              }
              return result;
            }

            var data = this.products
            const chunkSize = getChunkSize();
            var chunksv2 = chunkArray(this.data, chunkSize)
            chunksv2[0].is_active = true   
            this.$el.find('#top_products_carousel').html(
                renderToElement('tn_carousel_category.products_category_wise', {
                    chunksv2
                })
            )

            
            
        },
    })
