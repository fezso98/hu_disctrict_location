from odoo import api, fields, models
import logging

class CountryDisctrict(models.Model):
    _name = 'res.country.disctrict'
    _description = "Disctricts"
    _order = 'code'

    name = fields.Char(string='Disctrict Name', required=True,
               help='Administrative divisions of a county.')
    country_id = fields.Many2one('res.country', string='Country', required=True)
    state_id = fields.Many2one('res.country.state', string='State', domain="[('country_id', '=', country_id)]")
    code = fields.Char(string='Disctrict Code', help='The disctrict code', required=True)

    _sql_constraints = [
        ('name_code_uniq', 'unique(country_id, code)', 'The code of the state must be unique by country !')
    ]

    def _name_get(self):
        res = []
        for disctrict in self:
            name = disctrict.name if not disctrict.code else '%s (%s)' % (disctrict.name, disctrict.code)
            res.append((disctrict.id, name))
        return res

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        args = list(args or [])
        # optimize out the default criterion of ``ilike ''`` that matches everything
        if not (name == '' and operator == 'ilike'):
            args += ['|', (self._rec_name, operator, name), ('code', operator, name)]
        return self._search(args, limit=limit, access_rights_uid=name_get_uid)
