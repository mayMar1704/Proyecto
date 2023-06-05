# -*- coding: utf-8 -*-
# from odoo import http


# class EmpresaAbogados(http.Controller):
#     @http.route('/empresa_abogados/empresa_abogados', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/empresa_abogados/empresa_abogados/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('empresa_abogados.listing', {
#             'root': '/empresa_abogados/empresa_abogados',
#             'objects': http.request.env['empresa_abogados.empresa_abogados'].search([]),
#         })

#     @http.route('/empresa_abogados/empresa_abogados/objects/<model("empresa_abogados.empresa_abogados"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('empresa_abogados.object', {
#             'object': obj
#         })
