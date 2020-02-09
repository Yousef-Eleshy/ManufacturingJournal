# -*- coding: utf-8 -*-
# from odoo import http


# class ManufacturingJournal(http.Controller):
#     @http.route('/manufacturing_journal/manufacturing_journal/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/manufacturing_journal/manufacturing_journal/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('manufacturing_journal.listing', {
#             'root': '/manufacturing_journal/manufacturing_journal',
#             'objects': http.request.env['manufacturing_journal.manufacturing_journal'].search([]),
#         })

#     @http.route('/manufacturing_journal/manufacturing_journal/objects/<model("manufacturing_journal.manufacturing_journal"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('manufacturing_journal.object', {
#             'object': obj
#         })
