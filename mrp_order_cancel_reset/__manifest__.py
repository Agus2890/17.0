# -*- coding: utf-8 -*-
#############################################################################
#
#
#    Copyright (C) 2023-TODAY
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
{
    'name': 'mrp order cancel reset',
     'version': "18.0.1.0.0",
    'category': 'Manufacturing',
    'summary': 'reset draft Allows users reset to draft manufacturing order by clicking '
               'the button "CANCEL" reset workorder',
    'description': 'Allow users to cancel manufacturing orders',
    'author': 'Tecno Pos',
    'maintainer': '',
    'company': 'Tecno Pos',
    'price': 22,
    'currency': "USD",
    'website': '',
    'depends': ['base', 'mrp'],
    'data': [
        'security/cancel_mrp_order_groups.xml',
        'views/mrp_production_views.xml',
    ],
    'images': ['static/description/assets/image1.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
