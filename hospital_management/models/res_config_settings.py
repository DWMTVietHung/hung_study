# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = ['res.config.settings']

    number_of_days_to_expire = fields.Integer(string='Number of days to expire', config_parameter = 'hospital_management.number_of_days_to_expire')
