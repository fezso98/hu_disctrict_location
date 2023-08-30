from odoo import api, fields, models
import logging

_logger = logging.getLogger(__name__)

class ResCompany(models.Model):
    _inherit = "res.company"

    # In order to keep the same logic used in Odoo, fields must be computed
    # and inversed, not related. This way we can ensure that it works
    # correctly on changes and that inconsistencies cannot happen.
    # When you make the fields related, the constrains added in res.partner
    # will fail, because when you change the disctrict_id in the company, you are
    # effectively changing it in the partner. The constrains on the partner
    # are evaluated before the inverse methods update the other fields (city,
    # etc..) so we need them to ensure consistency.
    # As a conclusion, address fields are very related to each other.
    # Either you make them all related to the partner in company, or you
    # don't for all of them. Mixing both approaches produces inconsistencies.

    disctrict_id = fields.Many2one(
        "res.country.disctrict",
        compute="_compute_address",
        inverse="_inverse_disctrict_id",
        string="Disctrict ID",
    )

    def _get_company_address_field_names(self):
        """Add to the list of field to populate in _compute_address the new
        ZIP field + the city that is not handled at company level in
        `base_address_city`.
        """
        res = super()._get_company_address_field_names()
        res += ["disctrict_id"]
        return res
    
    def _inverse_disctrict_id(self):
        for company in self:
            company.partner_id.disctrict_id = company.disctrict_id

    @api.onchange("city")
    def _onchange_city(self):
        if self.city:
            self.update(
                {
                    "country_id": self.city.country_id,
                    "state_id": self.city.state_id,
                    "disctrict_id": self.city.disctrict_id,
                }
            )

    @api.onchange("disctrict_id")
    def _onchange_disctrict_id(self):
        if self.disctrict_id.state_id:
            self.state_id = self.disctrict_id.state_id.id


    @api.onchange("state_id")
    def _onchange_state_id(self):
        if self.state_id.country_id:
            self.country_id = self.state_id.country_id.id