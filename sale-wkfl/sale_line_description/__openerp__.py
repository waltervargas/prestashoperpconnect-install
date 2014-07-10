# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2013 Agile Business Group sagl
#    (<http://www.agilebg.com>)
#    @author Alex Comba <alex.comba@agilebg.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "Sale line description",
    'version': '0.1',
    'category': 'Sales Management',
    'description': """
This module allows to use only the product description on the sale order lines.
To do so, the user has to belong to group_use_product_description_per_so_line.
This is possible by selecting the related option in the following menu:

Settings --> Configuration --> Sale --> Sale Features
    """,
    'author': 'Agile Business Group',
    'website': 'http://www.agilebg.com',
    'license': 'AGPL-3',
    "depends": [
        'sale',
    ],
    "data": [
        'security/sale_security.xml',
        'res_config_view.xml',
    ],
    "active": False,
    "installable": True
}
