from odoo import fields, models, api
import logging

_logger = logging.getLogger(__name__)

class StateNSR(models.Model):
    _inherit = 'res.country.state'

    disctrict_ids = fields.One2many('res.country.disctrict', 'state_id', string='Disctricts')