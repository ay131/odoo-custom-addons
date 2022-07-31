
from datetime import date

from odoo import models, fields, api,_

#  patients model
class HospitalPatient(models.Model):
   _name = 'hospital.patient'
   _inherit=['mail.thread','mail.activity.mixin']
   _description = 'hospital patient'
   


   p_id=fields.Char(string='p_id',required=True,copy=False,readonly=True,default=lambda self:_('New'))
   name = fields.Char(string='name',required=True,tracking=True)
   age = fields.Integer(string='age',tracking=True,compute='_compute_age' ) 
   gender=fields.Selection([('male','male'),('female','female')],string='gender',tracking=True)
   img=fields.Binary(string='patient image')
   brith_date=fields.Date(string='date of birth')
   active=fields.Boolean(string='Active',default=True)
   appointments=fields.One2many('hospital.appointment','patient_id',string='appointments')
   appointment_count=fields.Integer(string='appointment count',compute="_compute_appointment_count")

   @api.model
   def create(self, vals):
      if  vals.get('p_id',_('New')) == _('New'):
         vals['p_id']=self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
         
      res= super(HospitalPatient,self).create(vals)
      return res

   # _compute_age founction 
   @api.depends('brith_date')
   def _compute_age(self):
      d_now=date.today()
      for i in self:
         if i.brith_date :
            # self.age = math.ceil((d_now.year - i.brith_date.year ) +( d_now.month - i.brith_date.month) / 12 )
            self.age =d_now.year - i.brith_date.year
         else:
            self.age = 1

   # _compute_appointment_count founction 
   def _compute_appointment_count(self):
     self.appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', self.id)])


