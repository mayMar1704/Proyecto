from odoo import models, fields, api
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class contactos(models.Model):
     _name = 'empresa_abogados.contactos'
     _description = 'empresa_abogados.contactos'
     _inherit='empresa_abogados.base'

     id = fields.Char(string='ID',required=True)
     id_c= fields.Many2one('empresa_abogados.clientes',string='Id Cliente',required=True)
     name = fields.Char(string='Nombre')   
     apellidos = fields.Char(string='Apellidos')   
     cargo = fields.Char(string='Cargo')
     numero = fields.Char(string='Telefono')
     correo = fields.Char(string='Correo')
   
class clientes(models.Model):
     _name='empresa_abogados.clientes'
     _description='Modelos para almacenar clientes'
     _inherit='empresa_abogados.base'
     
     name = fields.Char(string='Nombre',required=True)
     acronimos= fields.Char(string='Acronimo')
     id = fields.Char(string="ID Cliente",required=True,size=8)
     cif = fields.Char(string='CIF Propietario', size=9)
     tipologia = fields.Selection([('0','Organismo Publico'),('1','Empresa Privada (S.A)'),('2','Empresa Privada (S.L)'),('3','Persona fisica')],string='tipo cliente')
     direccion = fields.Char(string='Direccion')
     contactos = fields.Many2many('empresa_abogados.contactos')
    

