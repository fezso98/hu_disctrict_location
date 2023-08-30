{
    'name': 'Disctricts',
    'summary': """Add disctricts - as smaller part of county""",
    'version': '15.0.1.0.1',
    'sequence': '20',
    'description': """ Disctrict - Administrative divisions of a county. / Járások, mint adminisztrítiv területi egységek kezelése
                        """,
    'author': 'Keszisoft 2002 Bt.',
    'website': 'https://www.keszisoft.hu',
    'category': 'Hidden/Tools',
    'contributors': ['Fekete Zsolt <zsolt.fekete@keszisoft.hu>',],
    'depends': [
        'base', 'contacts', 'base_address_city',
        ],
    'license': 'AGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/jaras_views.xml',
        'views/orszag_views.xml',
        'views/partner_views.xml',

    ],
}
