from odoo import fields, models, api
from datetime import date, timedelta
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    date_use = fields.Integer(string="Date Used")
    date_expire = fields.Datetime(string="Date Expired")

    @api.onchange('date_use')
    def date_expire_change(self):
        self.date_expire = date(self.date_order.year, self.date_order.month, self.date_order.day) + timedelta(
            days=self.date_use)

    @api.onchange('date_expire')
    def date_use_change(self):
        if self.date_order and self.date_expire:
            self.date_use = (fields.Datetime.from_string(self.date_expire) - self.date_order).days + 1

    @api.constrains('date_use')
    def date_use_erro(self):
        if self.date_use < 0:
            raise ValidationError ("Date Used cannot be negative.")