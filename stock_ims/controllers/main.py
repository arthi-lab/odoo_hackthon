from odoo import http
from odoo.http import request

class IMSAuthController(http.Controller):

    @http.route('/ims/request_otp', type='json', auth='public')
    def request_otp(self, email):
        user = request.env['res.users'].sudo().search([('login', '=', email)], limit=1)
        if user:
            otp = user.generate_otp()
            # In a real app, send this via email/SMS
            # For now, we'll log it or return it for demo purposes if needed
            # return {'status': 'sent', 'otp': otp} # Security risk to return OTP
            return {'status': 'sent'}
        return {'status': 'user_not_found'}

    @http.route('/ims/verify_otp', type='json', auth='public')
    def verify_otp(self, email, otp, new_password):
        user = request.env['res.users'].sudo().search([('login', '=', email)], limit=1)
        if user and user.verify_otp(otp):
            user.sudo().write({'password': new_password})
            return {'status': 'success'}
        return {'status': 'invalid_otp'}

    @http.route('/web/reset_password', type='http', auth='public', methods=['POST'], website=True, sitemap=False)
    def password_reset_submit(self, **post):
        if post.get('otp'):
            email = post.get('login')
            otp = post.get('otp')
            password = post.get('password')
            user = request.env['res.users'].sudo().search([('login', '=', email)], limit=1)
            if user and user.verify_otp(otp):
                user.sudo().write({'password': password})
                return request.redirect('/web/login?message=password_reset')
            else:
                return request.render('auth_signup.reset_password', {
                    'error': 'Invalid OTP or expired.',
                    'login': email
                })
        return http.request.render('auth_signup.reset_password', post)
