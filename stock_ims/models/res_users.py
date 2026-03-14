from odoo import models, fields, api
import random
import string
import logging

_logger = logging.getLogger(__name__)

class ResUsers(models.Model):
    _inherit = 'res.users'

    otp_code = fields.Char(string='OTP Code', copy=False)
    otp_expiry = fields.Datetime(string='OTP Expiry', copy=False)

    def generate_otp(self):
        self.ensure_one()
        otp = ''.join(random.choices(string.digits, k=6))
        self.otp_code = otp
        self.otp_expiry = fields.Datetime.now() + fields.tools.datetime.timedelta(minutes=10)
        return otp

    def verify_otp(self, otp):
        self.ensure_one()
        if self.otp_code == otp and self.otp_expiry > fields.Datetime.now():
            self.otp_code = False  # Clear after use
            return True
        return False


