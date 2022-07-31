# -*- coding: utf-8 -*-
# from odoo import http


# class HospitalAsw(http.Controller):
#     @http.route('/hospital_asw/hospital_asw', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hospital_asw/hospital_asw/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hospital_asw.listing', {
#             'root': '/hospital_asw/hospital_asw',
#             'objects': http.request.env['hospital_asw.hospital_asw'].search([]),
#         })

#     @http.route('/hospital_asw/hospital_asw/objects/<model("hospital_asw.hospital_asw"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hospital_asw.object', {
#             'object': obj
#         })
