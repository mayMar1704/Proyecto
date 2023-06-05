
from odoo import models, fields, api
from datetime import datetime, timedelta
import re
from . import proyecto

class oferta(models.Model):
    _name='empresa_abogados.oferta'
    _description='Modelos para almacenar oferta'
    _inherit='empresa_abogados.base'
    
    name = fields.Char(string='Numero de oferta',required=True)
    fecha_solicitud_oferta= fields.Date(string='Fecha solicitud de la oferta',default=fields.Datetime.now)
    fecha_fin_plazo_ejecucion=fields.Date(string='Fecha Fin Plazo Ejecucion',default=fields.Datetime.now) 
    fecha_envio =fields.Date(string='Fecha Envio',default=fields.Datetime.now)
    proyecto_id = fields.Many2one('empresa_abogados.proyecto', string='Proyectos')
    aceptada= fields.Boolean(string='Aceptada')
    num_informes= fields.Integer(string='Num de Informes')
    convocatoria=fields.Char(string='Convocatoria')
   
    observaciones = fields.Text(string='Observaciones')

class estudio(models.Model):
    _name ='empresa_abogados.estudio'
    _description ='Modelos para almacenar estudio'
    
    _inherit='empresa_abogados.base'

    proyecto = fields.Many2one('empresa_abogados.proyecto',string="Proyecto",ondelete='cascade')
    name = fields.Char(string='CPV',required=True)
    contacto= fields.Text(string='Email de Contacto')
    Fin_plazo_presentacion_oferta = fields.Datetime(string='Fin plazo presentacion oferta') 
    importe_licitación = fields.Float(string='Importe licitacion')
    valor_estimado= fields.Float(string='Valor Estimado')
    plazo_de_ejecución = fields.Char(string='Plazo de Ejecucion') 
    posible_prorroga = fields.Text('Posible prorroga')
    criterios_objetivos = fields.Text(string='Criterios objetivos')
    criterios_subjetivos = fields.Text(string='Criterios subjetivos')
    solvencia_económica_exigida = fields.Text(string='Solvencia economica exigida')
    solvencia_técnica_exigida = fields.Text(string='Solvencia tecnica exigida')
    forma_presentación_oferta = fields.Text(string='Forma Presentacion Oferta')
    presentado = fields.Boolean(string='Presentado',default= False)
    fecha_presentacion = fields.Date(string='Fecha de Presentacion') 
    presentado_consorcio = fields.Boolean(string='Presentado en Consorcio',default= False)
    nombre_consorcio = fields.Char(string='Nombre del Consorcio',default= False)	
    equipo_trabajo_requerido = fields.Text(string='Equipo de trabajo Requerido')
    descartado = fields.Boolean(string='Descartado',default= False)
    motivo_descarte = fields.Text(string='Motivo de Descarte')
   
    @api.onchange('presentado')
    def _onchange_boolean(self):
        if self.presentado:
            self.descartado = False
        elif self.presentado == False:
            self.descartado = True

class seguimiento(models.Model):
    _name='empresa_abogados.seguimiento'
    _description='Modelos para el seguimiento de un proyecto'
    _inherit='empresa_abogados.base'
    id= fields.Integer(string ='id')
    proyecto =fields.Many2one('empresa_abogados.proyecto',string="Proyecto",ondelete='cascade')
    precio_arca_bi=fields.Integer(string='Precio Arca BI')
    baja_de_arca= fields.Float(string='Baja de Arca') 
    
    precio_empresa_adjudicataria=fields.Integer(string='Precio empresa adjudicataria')
    baja_empresa_adjudicataria=fields.Float(string='Baja empresa Adjudicataria') 
    puntuacion_OT_Arca=fields.Integer(string='Puntuacion OT Arca')
    puntuacion_OT_adjudicataria=fields.Integer(string='Puntuacion OT Adjudicataria')
    adjudicado=fields.Boolean(string='Adjudicado',default= False)
    nombre_empresa_adjudicataria = fields.Char(string='Nombre Empresa Adjudicado')
    _sql_constraints = [
    ('referencia_id_seguimiento', 'UNIQUE(id)', 'La referencia debe ser única.')]
class adjudicacion(models.Model):
     _name='empresa_abogados.adjudicacion'
     _description ='Modelos para la adjudicaccion estudio'
     _inherit='empresa_abogados.base'

     id=fields.Integer(string='ID')
     proyecto=fields.Many2one('empresa_abogados.proyecto',string='Proyecto',ondelete='cascade')
     fecha_fin_plazo_ejecucion=fields.Date(string='Fecha Fin Plazo Ejecucion (segun contrato)',default=fields.Datetime.now) 
     fecha_fin_plazo_prorroga=fields.Date(string='Fecha Fin Plazo ( con prorroga)',default=fields.Datetime.now) 
     fecha_de_adjudicacion=fields.Date(string='Fecha Contrato',default=fields.Datetime.now) 
     _sql_constraints = [
    ('referencia_id_adjc', 'UNIQUE(id)', 'La referencia debe ser única.')]
     