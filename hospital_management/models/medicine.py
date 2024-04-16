from odoo import models, fields, api
import io
import xlsxwriter
import base64
import tempfile

class Medication(models.Model):
    _name = 'medication'
    _description = 'Medication Information'

    name = fields.Char(string='Name', required=True)
    manufacturing_date = fields.Date(string='Manufacturing Date')
    expiry_date = fields.Date(string='Expiry Date')
    price = fields.Float(string='Price', required=True)
    file = fields.Binary(string='Exported File')

    def export_medicine_action(self):
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)

        worksheet = workbook.add_worksheet('Medication Information')

        header_format = workbook.add_format({'bold': True})
        worksheet.write_row(0, 0, ['Name', 'Manufacturing Date', 'Expiry Date', 'Price'], header_format)

        row = 1
        for medicine in self:
            worksheet.write_row(row, 0, [medicine.name, medicine.manufacturing_date, medicine.expiry_date, medicine.price])
            row += 1

        workbook.close()

        output.seek(0)
        excel_data = output.read()

        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx')
        temp_file.write(excel_data)
        temp_file.close()

        with open(temp_file.name, 'rb') as file:
            excel_binary = base64.b64encode(file.read())
        selected_records = self.env[self._name].browse(self.ids)
        selected_records.write({'file': excel_binary})

        return {
            'type': 'ir.actions.act_url',
            'url': 'web/content/?model=%s&id=%s&filename=ExportedMedication.xlsx&field=file&download=true' % (self._name, self.ids[0]),
            'target': 'self',
        }




class OderMedication(models.Model):
    _name = 'oder.medication.line'
    _description = 'Medication Information'
    _rec_name = "name_medicine"

    name_medicine = fields.Many2one('medication', string="Medication")
    description = fields.Text(string='Description')
    quantity = fields.Float(string="Quantity", default=1)
    price_unit = fields.Float(string="Unit Price", compute='_compute_price_unit', store=True)
    tax_id = fields.Many2many(comodel_name='account.tax', string="Tax")
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

