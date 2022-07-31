# -*- coding: utf-8 -*-
{
    'name': "hospital management ",

    'summary': "hospital management system for all hospitalllll lllll",

    'description': "hospital management system",
    'sequence':-100,
 

    'author': "abyo Company",
    'website': "http://www.abyocompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'hospital',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale','base','mail','product'],

    # always loaded
    'data': [
        # security
        'security/ir.model.access.csv',
        # data
        'data/data.xml',
        # wizard
        'wizard/create_appoientment_view.xml',
        'wizard/appiontment_report_view.xml',
       
        # views
        
        'views/patient.xml',
        'views/appointment.xml',
        'views/doctor.xml',
        'views/menu.xml',
        # report
        'report/report_temp_patient.xml',
        'report/report_temp_appointment.xml',
        'report/report_temp_doctor.xml',
        'report/report.xml',
  
   
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
