from unicodedata import name
from odoo import models, fields, api, _
# create appointment model
class CreateAppointmentWizard(models.TransientModel):
    #  ========================model title========================
    _name = 'create.appointment.wizard'
    _description = 'create appointment wizard'

# ===============================================================================
# =======================================[main fields]=========================
    appointment_date = fields.Datetime(string='appointment date', required=True)
    is_available = fields.Boolean(string='available y/n')
# ===============================================================================
# =======================================[relation fields]=========================
    doctor = fields.Many2many('hospital.asw.doctor', string='doctor')
# =================================================================================
# =======================================[class method]=========================
    def action_create_appointment(self):
        vals = {
            'appointment_date': self.appointment_date,
            'is_available': self.is_available,
            'doctor': self.doctor,
        }
        appointment_id = self.env['hospital.appointment'].create(vals)
        return {
            'name': _('Create Appointment'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hospital.appointment',
            'res_id':appointment_id.id ,
            'target': 'now',
        }
 # =================================================================================
