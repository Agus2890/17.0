{
    'name': "POS - pos defined discount",
    'description': "Allows POS to have defined and custom discounts",
    'summary': "Allows POS to have defined and custom discounts",
    'author': "Tecno Pos",
    'website': "",
    'category': 'Point of Sale',
    'module_type': 'official',
    'price': 25,
    'currency': "USD",
    'version': '1.0',
    'depends': ['point_of_sale'],
    'images': ['static/description/icon.png'],
    'license': 'OPL-1',
    "data": [
        'security/ir.model.access.csv',
        'security/group_discount.xml',
        'views/res_config_settings_inherit.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_defined_discount/static/src/**/*',
        ],
    }
}
