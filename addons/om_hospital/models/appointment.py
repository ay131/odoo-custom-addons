
from datetime import date  
from email.policy import default

from attr import field
from odoo import models, fields, api,_


stat=[
      ('draft','Draft'),
      ('in_consultation','In_Consultation'),
      ('done','Done'),
      ('cancalled','Cancalled'),
   ]
per=[
   ('0','normal'),
   ('1','low'),
   ('2','high'),
   ('3','very high'),
]


# appointment model
class HospitalAppointment(models.Model):
   _name = 'hospital.appointment'
   _inherit=['mail.thread','mail.activity.mixin']
   _description = 'hospital appointment'
   _rec_name = 'patient_id'




  
   appointment_id=fields.Char(string='id',required=True,copy=False,readonly=True,default=lambda self:_('New'))
   patient_id=fields.Many2one('hospital.patient',string='patient')

   gender=fields.Selection(related='patient_id.gender')
   appointment_date=fields.Date(string='appointment time' , default=date.today())
   booking_date=fields.Date(string='booking date')
   description=fields.Char(string='description')

   pharmacy=fields.One2many('appointment.pharmacy','appointment_ids',string='pharmacy')
   predescription=fields.Html(string='predescription')
   priority=fields.Selection(selection=per,string='priority')
   state=fields.Selection(selection=stat,string='state',required=True,default='draft')
   doctor_id=fields.Many2one('hospital.doctor',string='doctor')
   img=fields.Binary(related='patient_id.img')
   
# action_do_cancal
   def action_do_cancal (self):
      self.state  ='cancalled'
      return {
                'effect': {
                    'fadeout': 'slow',
                    'message': 'appointment cancalled successfully ',
                    'type': 'rainbow_man',
                }
            }
            
# action_do_in_consultation
   def action_do_in_consultation (self):
      self.state  ='in_consultation'

# action_do_done
   def action_do_done (self):
      self.state  ='done'
 
# onchange_patient_id
   @api.onchange('patient_id')
   def onchange_patient_id(self):
      self.p_id=self.patient_id.p_id

# over ridde create action 
   @api.model
   def create(self, vals):
      if not vals.get('priority'):
         vals['priority']='1'
         
      res= super(HospitalAppointment,self).create(vals)
      return res

# over ridde create action 
   @api.model
   def create(self, vals):
      if  vals.get('appointment_id',_('New')) == _('New'):
         vals['appointment_id']=self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
         
      res= super(HospitalAppointment,self).create(vals)
      return res

# appointment.pharmacy model 
class AppointmentPharmacy(models.Model):
   _name = 'appointment.pharmacy'
   _description = 'hospital appointment Pharmacy'

   product_id=fields.Many2one('product.product',required=True)
   price_unit=fields.Float(string='price' ,related='product_id.list_price')
   qty=fields.Integer(string='quantity',default=1)
   appointment_ids=fields.Many2one('hospital.appointment' ,string='appointment_ids')
