from odoo import fields, models, api, _
from odoo.exceptions import  ValidationError
# =================const data ==========================
stat = [
    ('draft', 'Draft'),
    ('in_progress', 'In Progress'),
    ('done', 'Done'),
    ('cancal', 'Cancal'),
]


# =================class defination==========================
class Reception(models.Model):
    _name = 'reception'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'hospital  reception'
    _rec_name = 'reception_id'
    # ================normal fields====================
    reception_id = fields.Char(string='reception', required=True, copy=False, readonly=True,
                               default=lambda self: _('New'))
    active = fields.Boolean(string='Active', default=True)
    state = fields.Selection(selection=stat, string='state', default='draft', tracking=True)
    description = fields.Char(string='description', required=True, tracking=True)

    # ================relations fields====================
    patient_name = fields.Many2one('hospital.asw.patient', string='patient name')
    doctor_reservation = fields.Many2many('hospital.asw.doctor', string='doctor name')
    appointment_dt = fields.Many2many('hospital.appointment', string='dappointment date')

    # ================stateusbar actions====================
    def action_do_in_progress(self):
        self.state = 'in_progress'

    # --------------------------
    def action_do_done(self):
        self.state = 'done'

    # --------------------------
    def action_do_cancal(self):
        self.state = 'cancal'

    # ================[create overrid]====================
    @api.model
    def create(self, vals):
        if vals.get('reception_id', _('New')) == _('New'):
            vals['reception_id'] = self.env['ir.sequence'].next_by_code('rec.sequence') or _('New')
        res = super(Reception, self).create(vals)
        for appintment in res.appointment_dt:
            res_appintment = self.env['hospital.appointment'].search([('appointment_date', '=',appintment.appointment_date)])
            if res_appintment.exists():
                for evry_appintment in res_appintment:
                    evry_appintment.write({
                        'is_available': False,
                        'patient_id': res.patient_name,
                    })
        return res

    # ========================== on change ================
    @api.onchange('doctor_reservation')
    def _onchange_doctor_reservation(self):
        for res in self.doctor_reservation.appointment_id:
            if res.is_available == True:
                self.appointment_dt = res
            else:
                raise ValidationError(_('there no avaliable  appointment for this doctor'))



    # if self.doctor_reservation:
    #     for all_doctor in self.doctor_reservation.appointment_id:
    #         self.appointments.appointment_date.pop(all_doctor.appointment_date)
    #         # res.append(self.appointments.is_available)
    #
