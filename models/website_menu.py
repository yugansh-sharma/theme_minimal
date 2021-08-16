# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class Website(models.Model):
    _inherit = 'website.menu'

    icon_image = fields.Binary("Menu Icon")
