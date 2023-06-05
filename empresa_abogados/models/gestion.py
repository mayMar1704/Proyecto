from odoo import models, fields, api
from datetime import datetime, timedelta

class gestion(models.Model):
     _name='empresa_abogados.gestion'
     _description='proyecto'
     _inherit='empresa_abogados.base'
     proyectos = fields.Many2one('empresa_abogados.proyecto', string='Proyecto',ondelete='cascade')
    
     id = fields.Char(string="id",required=True,size=8)
     area = fields.Char(string='Area')
     certificado = fields.Boolean(string='Certificado')
     tramitacion = fields.Selection(related='proyectos.tramitacion', string='Tramitación')
     facturado = fields.Boolean(string="Facturado")
     ejecutado= fields.Boolean(string="Ejecutado")
     fecha_finalizacion = fields.Date(string="Fecha de Finalizacion",default=lambda self: fields.Date.today())
     fecha_cierre = fields.Date(string="Fecha de Cierre",default=lambda self: fields.Date.today())