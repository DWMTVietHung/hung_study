from odoo import fields, models, api


class ContactHospital(models.Model):
    _inherit = 'res.partner'

    specialist = fields.Selection([
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
        ('patient', 'Patient')
    ], string='Specialist', default='doctor')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', default='male')
    medication_order_lineids= fields.One2many("oder.medication.line","order_id")
    