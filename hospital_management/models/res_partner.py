from odoo import fields, models, api


class HrEmployee(models.Model):
    _inherit = 'res.partner'

    specialist = fields.Selection([
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
        ('patient', 'Patient')
    ], string='Specialist', default='doctor')

    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', default='male')
