# -*- coding: utf-8 -*-
###############################################################################
#
#   Copyright (C) 2013-TODAY Akretion <http://www.akretion.com>.
#     All Rights Reserved
#     @author David BEAL <david.beal@akretion.com>
#     Sébastien BEAU <sebastien.beau@akretion.com>
#     Guewen Baconnier (camptocamp)
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from openerp.osv import orm

class prestashoperpconnect_pricelist_installed(orm.AbstractModel):
    """Empty model used to know if the module is installed on the
    database.

    If the model is in the registry, the module is installed.
    """
    _name = 'prestashoperpconnect_pricelist.installed'

