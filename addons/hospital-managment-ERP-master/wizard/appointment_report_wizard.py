from odoo import models, fields, api,_
 
class AppointmentReportWizard(models.TransientModel):

    _name = 'appointment.report.wizard'
    _description = 'create report wizard'

    patient_id=fields.Many2one('hospital.patient',string='patient')
    date_from=fields.Date(string='date from' )
    date_to=fields.Date(string='date to')
    


    def appointment_report_action(self):
        domain=[]
        if self.patient_id:
            domain+=[('patient_id','=',self.patient_id.id)]
            
        if self.date_from:
            domain+=[('appointment_date','>=',self.date_from)]
            
        if self.date_to:
            domain+=[('appointment_date','<=',self.date_to)]
            
        appointments=self.env['hospital.appointment'].search_read(domain)
        data={
            'form':self.read()[0],
            'appointments':appointments,
            
        }
        return self.env.ref('om_hospital.appointment_reports_action').report_action(self,data=data)
      