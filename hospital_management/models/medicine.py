from odoo import models, fields, api
from collections import defaultdict


class Medication(models.Model):
    _name = 'medication'
    _description = 'Medication Information'

    name = fields.Char(string='Name', required=True)
    manufacturing_date = fields.Date(string='Manufacturing Date')
    expiry_date = fields.Date(string='Expiry Date')
    price = fields.Float(string='Price', required=True)


class OderMedication(models.Model):
    _name = 'oder.medication.line'
    _description = 'Medication Information'
    _rec_name = "name_medicine"

    name_medicine = fields.Many2one('medication', string="Medication")
    description = fields.Text(string='Description')
    quantity = fields.Float(string="Quantity", default=1)
    price_unit = fields.Float(string="Unit Price", compute='_compute_price_unit', store=True)
    tax_id = fields.Many2many(comodel_name='account.tax', string="Taxes")
    price_subtotal = fields.Float(string="Subtotal")

    order_id = fields.Many2one('res.partner', string="Order Reference")

    @api.depends('name_medicine.price')
    def _compute_price_unit(self):
        for record in self:
            record.price_unit = record.name_medicine.price if record.name_medicine else 0.0

    @api.onchange('quantity', 'price_unit')
    def _onchange_quantity_price_unit(self):
        for record in self:
            record.price_subtotal = record.quantity * record.price_unit

