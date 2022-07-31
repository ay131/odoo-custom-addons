
from odoo import models, fields, api,_

# appointment model
class HospitalAswDoctor(models.Model):
   _name = 'hospital.asw.doctor'
   _inherit=['mail.thread','mail.activity.mixin']
   _description = 'hospital aswan doctors'
   _rec_name='doctor_name'

   doctor_id=fields.Char(string='id',required=True,copy=False,readonly=True,default=lambda self:_('New'))
   doctor_name=fields.Char(string='name',required=True)
   doctor_img=fields.Binary(string='patient image')
   doctor_gender=fields.Selection([('male','male'),('female','female')],string='gender',tracking=True)
   doctor_specialization=fields.Many2one('specialization',string='specialization')
   appointment_id=fields.Many2many('hospital.appointment',string='appointments')

   @api.model
   def create(self, vals):
      if  vals.get('doctor_id',_('New')) == _('New'):
          vals['doctor_id']=self.env['ir.sequence'].next_by_code('hospital.asw.doctor') or _('New')
      res= super(HospitalAswDoctor,self).create(vals)
      return res



   
