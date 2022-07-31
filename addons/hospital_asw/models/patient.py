# -*- coding: utf-8 -*-

from datetime import date

from odoo import models, fields, api,_

#  patients model
class HospitalAswPatient(models.Model):
   _name = 'hospital.asw.patient'
   _inherit=['mail.thread','mail.activity.mixin']
   _inherits={'res.partner':'partner_id'}
   _description = 'hospital  aswan patient'
   


   patient_id=fields.Char(string='p_id',required=True,copy=False,readonly=True,default=lambda self:_('New'))
   patient_age = fields.Integer(string='age',compute='_compute_age',tracking=True, store=True)
   patient_gender=fields.Selection([('male','male'),('female','female')],string='gender',tracking=True)
   brith_date=fields.Date(string='date of birth')
   active=fields.Boolean(string='Active',default=True)
   partner_id = fields.Many2one("res.partner")

   # pharmacy=fields.One2many('hospital.pharmacy','pharmacy_id',string='pharmacy')

   appointments=fields.One2many('hospital.appointment','patient_id',string='appointments')
   # create overrid
   @api.model
   def create(self, vals):
      if  vals.get('patient_id',_('New')) == _('New'):
         vals['patient_id']=self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
      res= super(HospitalAswPatient,self).create(vals)
      res.partner_id.is_patient = True
      return res

   # _compute_age founction 
   @api.depends('brith_date')
   def _compute_age(self):
      for patient in self:
         data_now=date.today()
         if patient.brith_date :
            patient.patient_age =data_now.year - patient.brith_date.year
         else:
            patient.patient_age = 0

