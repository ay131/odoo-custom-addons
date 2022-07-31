from odoo import models, fields, api,_





# create appointment model
class CreateAppointmentWizard(models.TransientModel):
   _name = 'create.appointment.wizard'
   _description = 'create appointment wizard'
   

   booking_date=fields.Date(string='booking date',required=True)
   patient_id=fields.Many2one('hospital.patient',string='patient')


   def create_appointment_action(self):
       vals={
           'booking_date':self.booking_date,
           'patient_id': self.patient_id.id,
           
       }
       appointment_id=self.env['hospital.appointment'].create(vals)
       return {
           'name':_('Appointment'),
           'type':'ir.actions.act_window',
           'view_mode':'form',
           'res_model':'hospital.appointment',
           'res_id':appointment_id.id,
           'target':'now',
       }