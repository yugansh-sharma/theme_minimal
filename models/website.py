# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class Website(models.Model):
    _inherit = 'website'

    shop_ppr = fields.Integer(default=3, string="Number of grid columns on the shop")
