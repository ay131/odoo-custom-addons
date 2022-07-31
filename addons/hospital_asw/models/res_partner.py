from odoo import fields, models, api

class ResPartner(models.Model):
    _inherit = "res.partner"

    is_patient = fields.Boolean(string='is patient',default=False)
