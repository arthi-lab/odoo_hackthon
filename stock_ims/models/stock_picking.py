from odoo import models, fields, api, _
from odoo.exceptions import UserError

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def action_ims_validate(self):
        """ 
        Streamlined validation for IMS. 
        Automatically assigns, checks availability, and validates in one click.
        """
        self.ensure_one()
        if self.state == 'draft':
            self.action_confirm()
        if self.state not in ('assigned', 'done', 'cancel'):
            self.action_assign()
        
        # Immediate transfer logic (similar to Odoo's button_validate but more direct)
        return self.button_validate()

    def action_quick_receipt(self, product_id, qty, location_dest_id):
        """ helper method for API or custom UI calls """
        # Implementation for quick receipt logic
        pass
