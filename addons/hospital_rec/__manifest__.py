# -*- coding: utf-8 -*-
{
    'name': "hospital_rec",

    'summary': " hospital rec ",
    'description': "hospital reception module",

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'sequence': -100,


    'category': 'Uncategorized',
    'version': '0.1',
    'application': 'Ture',

    # any module necessary for this one to work correctly
    'depends': ['base','hospital_asw','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',


        'views/appointment.xml',
        'views/doctor.xml',
        'views/reception.xml',
        'views/patient.xml',
        'views/menu.xml',

        'data/data.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
