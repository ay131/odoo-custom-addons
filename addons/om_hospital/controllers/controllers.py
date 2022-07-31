# -*- coding: utf-8 -*-
# from odoo import http


# class Abyo(http.Controller):
#     @http.route('/abyo/abyo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abyo/abyo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('abyo.listing', {
#             'root': '/abyo/abyo',
#             'objects': http.request.env['abyo.abyo'].search([]),
#         })

#     @http.route('/abyo/abyo/objects/<model("abyo.abyo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abyo.object', {
#             'object': obj
#         })
