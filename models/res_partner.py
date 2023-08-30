from odoo import api, fields, models
import logging

_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    _inherit = 'res.partner'

    disctrict_id   = fields.Many2one('res.country.disctrict', string='Disctrict' )

    @api.model
    def _address_fields(self):
        """Returns the list of address fields that are synced from the parent."""
        return super()._address_fields() + ["disctrict_id"]
