# -*- coding: utf-8 -*-
{
    'name': "hospital_asw",

    'summary': "aswan hospital management system" ,
    'description': "aswan hospital management system",

    'author': "aswan hospital",
    'website': "http://www.yourcompany.com",

    'sequence': -100,

    'category': 'Uncategorized',
    'version': '0.1',
    'application': 'Ture',
    # any module necessary for this one to work correctly
    'depends': ['base','sale', 'mail', 'product','contacts'],

    # always loaded
    'data': [

        'security/ir.model.access.csv',

        'wizard/create_appointment_wizard.xml',



        'views/appointment.xml',
        'views/specialization.xml',
        'views/partner.xml',
        'views/patient.xml',
        'views/doctor.xml',
        'views/menu.xml',

        'data/data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}












