from odoo import fields, models, api
import logging

_logger = logging.getLogger(__name__)

class CountryDisctrict(models.Model):
    _inherit = 'res.country'

    disctrict_ids = fields.One2many('res.country.disctrict', 'country_id', string='Disctricts')