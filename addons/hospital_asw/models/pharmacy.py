# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

#  HospitalPharmacy model
class HospitalPharmacy(models.Model):
    _name = 'hospital.pharmacy'
    _inherit = ['product.product']
    _description = 'hospital  Pharmacy'

    pharmacy_id = fields.Many2one('hospital.asw.patient', string='pharmacy')

