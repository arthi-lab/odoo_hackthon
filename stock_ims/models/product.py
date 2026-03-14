from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def check_low_stock(self):
        """ Broad check for items below a certain threshold """
        low_stock_products = self.search([('qty_available', '<', 5)])
        for product in low_stock_products:
            _logger.info("IMS Alert: Low stock for %s", product.name)
        return True
