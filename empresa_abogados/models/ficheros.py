from odoo import models, fields, api,exceptions
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError
class Archivo(models.Model):
    _name = 'empresa_abogados.documento'
    _description = 'Modelo para guardar archivos'
    _inherit='ir.attachment'
    
    proyecto_id = fields.Many2one('empresa_abogados.proyecto', string='Proyecto')
    name = fields.Char(string='Nombre', required=False)
    @api.model
    def create(self, vals):
        if 'proyecto_id' in vals:
            proyecto_id = vals.get('proyecto_id')
            vals['res_id'] = proyecto_id
        return super(Archivo, self).create(vals)
    @api.constrains('name')
    def _check_name(self):
        for archivo in self:
            if not archivo.name:
                raise ValidationError('El campo Nombre es obligatorio.')

class IrAttachment(models.Model):
    _description = 'modulo ir.attachment modificado'
    _inherit = 'ir.attachment'
    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        args.append(('res_id', '!=', 0))
        return super(IrAttachment, self).search(args, offset=offset, limit=limit, order=order, count=count)
    @api.model_create_multi
    def create(self, vals_list):
        # Filtrar los registros con res_id igual a 0 y eliminarlos
        vals_list_filtered = [vals for vals in vals_list if vals.get('res_id', 0) != 0]
        return super(IrAttachment, self).create(vals_list_filtered)