
from odoo import models, fields, api,_

# appointment model
class HospitalDoctor(models.Model):
   _name = 'hospital.doctor'
   _inherit=['mail.thread','mail.activity.mixin']
   _description = 'hospital doctors'

   doctor_id=fields.Char(string='id',required=True,copy=False,readonly=True,default=lambda self:_('New'))
   name=fields.Char(string='name',required=True)
   img=fields.Binary(string='patient image')
   gender=fields.Selection([('male','male'),('female','female')],string='gender',tracking=True)
   specialization=fields.Char(string='specialization')
   appointments=fields.One2many('hospital.appointment','doctor_id',string='appointments',readonly=True)
   appointment_count_dector=fields.Integer(string='appointment count',compute="_compute_appointment_count_dector")
   @api.model
   def create(self, vals):
      if  vals.get('doctor_id',_('New')) == _('New'):
          vals['doctor_id']=self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
      res= super(HospitalDoctor,self).create(vals)
      return res



   
# _compute_appointment_count founction 
# @api.depends('')
   def _compute_appointment_count_dector(self):
      self.appointment_count_dector = self.env['hospital.appointment'].search_count([('doctor_id', '=', self.id)])


