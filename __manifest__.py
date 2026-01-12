# noinspection PyStatementEffect
{
    'name': 'Gestion des Courriers',
    'version': '1.0',
    'summary': 'Gestion des courriers entrants et sortants',
    'author': 'KABIL Youssef',
    'category': 'Administration',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/courrier_views.xml',
    ],
    'installable': True,
    'application': True,
}
