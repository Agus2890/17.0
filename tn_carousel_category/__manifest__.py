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
{
    'name': 'carrusel Category Snippet',
    'version': '17.0.1.0.0',
    'category': 'eCommerce',
    'summary': """Show Most Sold category in Website Based On product""",
    'description': """Showcase top most sold products on your website based on 
     category.If products are more a carousel will appear on each category.Using 
     view all button go directly to shop for products under that category.""",
    'author': 'Tecno Pos',
    'company': 'Tecno Pos',
    'maintainer': 'Tecno Pos',
    'website': '',
    'price': 20,
    'currency': "USD",
    'depends': ['website_sale'],
    'data': [
        "views/product_breadcrumb_templates.xml",
        "views/top_products_category_wise_templates.xml",
    ],
    'assets': {
        'web.assets_frontend': [
            'tn_carousel_category/static/src/js/top_selling_'
            'products.js',
            'tn_carousel_category/static/src/xml/top_products_'
            'templates.xml',
            'tn_carousel_category/static/src/css/products_'
            'carousel.css',
        ]},
    'images': ['static/description/banner.jpg'],
    'license': 'LGPL-3',
    'installable': True,
    'auto-install': False,
    'application': False,
}
