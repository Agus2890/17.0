from odoo import fields, models

class discountPos(models.Model):
    _name = "pos.custom.discount"
    
    custom_discount_name = fields.Char(string="Descripcion", required=True)#, readonly="pos_config_id.pos_has_active_session"
    custom_percentage = fields.Float(string="Descuento %", required=True)#, readonly="pos_config_id.pos_has_active_session"
    pos_config_id = fields.Many2one(string="Point of Sale Config", comodel_name="pos.config")