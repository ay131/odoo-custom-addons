
from odoo import models, fields, api,_

# appointment model
class Specialization(models.Model):
   _name = 'specialization'
   _description = 'doctor specialization'
   _rec_name='specialization'
   _sql_constraints = [
        ('specialization', 'unique (specialization)', 'specialization is dupplecated!'),
    ]

   name=fields.Char(string='Name',required=True,copy=False,readonly=True,default=lambda self:_('New'))
   specialization=fields.Char(string='specialization')

   @api.model
   def create(self, vals):
      if  vals.get('name',_('New')) == _('New'):
          vals['name']=self.env['ir.sequence'].next_by_code('specialization.sequence') or _('New')
      res= super(Specialization,self).create(vals)
      return res

   def name_get(self):
       res = []
       for rec in self:
           res.append((rec.id,'%s' % (rec.specialization)))
       return res



   
