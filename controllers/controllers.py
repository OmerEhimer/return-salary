# -*- coding: utf-8 -*-
from odoo import http

# class ReturnSalary(http.Controller):
#     @http.route('/return_salary/return_salary/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/return_salary/return_salary/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('return_salary.listing', {
#             'root': '/return_salary/return_salary',
#             'objects': http.request.env['return_salary.return_salary'].search([]),
#         })

#     @http.route('/return_salary/return_salary/objects/<model("return_salary.return_salary"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('return_salary.object', {
#             'object': obj
#         })