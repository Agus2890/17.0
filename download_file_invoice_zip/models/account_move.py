# -*- coding: utf-8 -*-
from odoo import api, fields, models, SUPERUSER_ID
from odoo.exceptions import AccessError, UserError, ValidationError
from datetime import datetime,timedelta
import pytz
tz = pytz.timezone('America/Mexico_City')

class AccountMove(models.Model):
    _inherit = "account.move"

    def action_get_files_cfdi(self):
        active_ids=self.env.context.get('active_ids')
        return {
            "type": "ir.actions.act_url",
            "url": f'/generate_zip?inv_ids={active_ids}',
            "target": "self",
        }