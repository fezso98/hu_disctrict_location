{
    'name': 'Districts',
    'summary': """Add districts - as smaller part of county""",
    'version': '15.0.1.0.1',
    'sequence': '20',
    'description': """ Disctrict - Administrative divisions of a county. / Járások, mint adminisztrítiv területi egységek kezelése
                        """,
    'author': 'Keszisoft 2002 Bt.',
    'website': 'https://www.keszisoft.hu',
    'category': 'Hidden/Tools',
    'contributors': ['Fekete Zsolt <zsolt.fekete@keszisoft.hu>',],
    'depends': [
        'base', 'contacts',
        ],
    'license': 'AGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/orszag_views.xml',
        'views/jaras_views.xml',
    ],
}
