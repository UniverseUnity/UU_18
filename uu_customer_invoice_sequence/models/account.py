from odoo import models, fields, api
from datetime import datetime


class AccountMove(models.Model):
    _inherit = "account.move"

    @api.model
    def create(self, vals):
        if vals.get("move_type") == "out_invoice" and not vals.get("name") or vals["name"] == "/":
            sequence_id = self.env.ref("uu_customer_invoice_sequence.seq_invoice_custom")
            current_year = datetime.now().year
            sequence_id.prefix = f"UUS/{current_year}/"
            vals["name"] = sequence_id.next_by_id()
        return super(AccountMove, self).create(vals)
