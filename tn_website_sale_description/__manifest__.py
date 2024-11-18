# © 2020 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "tn Website Product Description",
    "category": "Website",
    "summary": "Shows custom e-Commerce description for products",
    "version": "17.0.1.0.0",
    "website": "",
    "author": "Tecno Pos",
    'price': 6,
    'currency': "USD",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["website_sale"],
    "data": [
        "views/website_sale_template.xml",
        "views/product_template.xml",
    ],
    "demo": [
        "data/demo_website_sale_product_description.xml",
    ],
    "images":["static/description/assets/img1.jpg"],
}
