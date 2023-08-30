from odoo import fields, models, api
import logging

_logger = logging.getLogger(__name__)

class CityDisctrict(models.Model):
    _inherit = 'res.city'

    disctrict_id = fields.Many2one('res.country.disctrict', string='Disctricts', domain="[('state_id', '=', state_id)]")

    