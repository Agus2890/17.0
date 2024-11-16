"""Top-selling products controller"""
# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Jumana Haseen (<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from odoo import http
from odoo.http import request


class TopSellingProducts(http.Controller):
    @http.route(['/category_ecomerce_product'], type="json", auth="public", website=True, methods=['POST'])
    def get_products_categories(self):
        public_categ_ids = request.env['product.public.category'].sudo().search_read(
            [('parent_id', '=', False)], fields=['name', 'website_id','image_1920'])
        public_categories = []
        for category in public_categ_ids:
            products_search_read = request.env['product.template'].with_user(
                request.env.ref('base.user_admin')).search_read(
                [('is_published', '=', True),
                 ('public_categ_ids.id', '=', category['id'])],fields=['name', 'image_1920', 'public_categ_ids', 'website_id','sales_count'],limit=1 )
            for product in products_search_read:
                public_categories.append(category)
        return public_categories
