# -*- coding: utf-8 -*-
# from odoo import http


# class HospitalRec(http.Controller):
#     @http.route('/hospital_rec/hospital_rec', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hospital_rec/hospital_rec/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hospital_rec.listing', {
#             'root': '/hospital_rec/hospital_rec',
#             'objects': http.request.env['hospital_rec.hospital_rec'].search([]),
#         })

#     @http.route('/hospital_rec/hospital_rec/objects/<model("hospital_rec.hospital_rec"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hospital_rec.object', {
#             'object': obj
#         })
