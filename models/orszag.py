from odoo import fields, models, api
import logging

_logger = logging.getLogger(__name__)

class CountryNSR(models.Model):
    _inherit = 'res.country'

    nsr_id  = fields.Integer(string='NSR ID', index=True, group_operator=False)
    disctrict_ids = fields.One2many('res.country.disctrict', 'country_id', string='Disctricts')