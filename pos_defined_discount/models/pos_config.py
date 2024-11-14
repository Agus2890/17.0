from odoo import fields, models

class discountConfig(models.Model):
    _inherit = "pos.config"
    
    pos_custom_discount_ids = fields.One2many(string="Discounts", comodel_name="pos.custom.discount", inverse_name="pos_config_id")
    
    def get_discount_group(self):
        group_name = "pos_custom_predifined_discounts.group_discount"
        
        if not group_name:
            raise ValueError("Group not found")
        else:
            if self.env.user.has_group('pos_custom_predifined_discounts.group_discount'):
                return True
            else:
                return False