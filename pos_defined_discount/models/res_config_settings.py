from odoo import fields, models

class discountConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"
    
    pos_custom_discount_ids = fields.One2many(string="Discounts", comodel_name="pos.custom.discount", readonly=False, related="pos_config_id.pos_custom_discount_ids")
    
    