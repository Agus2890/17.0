from odoo import models

class PosSession(models.Model):
    _inherit = 'pos.session'

    def _pos_ui_models_to_load(self):
        res = super()._pos_ui_models_to_load()
        res += ["pos.custom.discount"]
        return res
    
    def _get_pos_ui_pos_custom_discount(self, params):
        disc = self.env["pos.custom.discount"].search_read(**params["search_params"])
        return disc
    
    def _loader_params_pos_custom_discount(self):
        return {
            "search_params": {
                "domain": [("pos_config_id", "=", self.config_id.id)],
                "fields": ["custom_discount_name", "custom_percentage",],
            },
        }
        
    def get_pos_ui_pos_custom_discount(self):
        return self._get_pos_ui_pos_custom_discount(self._loader_params_pos_custom_discount())
    