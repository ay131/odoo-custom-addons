import datetime

from odoo import models, fields, api, _


class HospitalAppointment(models.Model):
    #  ========================model title========================
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'hospital appointment'
    _rec_name = 'appointment_date'

    # =======================================[main fields]=========================
    appointment_id = fields.Char(string='appintment', required=True, copy=False, readonly=True,
                                 default=lambda self: _('New'))
    is_available = fields.Boolean(string='available y/n')
    appointment_date = fields.Datetime(string='appointment date', required=True)

    # =======================================[relation fields]=========================
    doctor = fields.Many2many('hospital.asw.doctor', string='doctor', required=True)
    patient_id = fields.Many2one('hospital.asw.patient', string='patient')
    # =======================================[over ridde]=========================
    # ======================== over ridde create action
    @api.model
    def create(self, vals):
        if vals.get('appointment_id', _('New')) == _('New'):
            vals['appointment_id'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _('New')
        res = super(HospitalAppointment, self).create(vals)
        return res

    # ==========================over ridde name_get
    def name_get(self):
        res = []
        for appoint in self:
            for seq in appoint.appointment_id:
                if appoint.is_available == True:
                    res_available = 'avaliable'
                else:
                    res_available = 'not avaliable'
                res.append(
                    (appoint.id, "[%s]%s[%s]" % (appoint.appointment_id, appoint.appointment_date, res_available)))
        return res
    # ========================== on change ================
    # @api.onchange('doctor','appointment_date')
    # def _onchange_doctor(self):
    #     res = self.env['hospital.asw.doctor'].search([])
    #     # for dr in res:
    #     #     if self.doctor.doctor_name == dr.doctor_name:
    #     #         dr.appointment_id.appointment_date =self.appointment_date
    #     #     else:
    #     #         dr.appointment_id.appointment_date = self.appointment_date
    #     print(res)
    #     # for all_doctor in self.doctor:
    #     #     self.appointments.appointment_date.pop(all_doctor.appointment_date)
    #     # res.append(self.appointments.is_available)
    #
