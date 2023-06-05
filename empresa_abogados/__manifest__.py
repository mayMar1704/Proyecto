# -*- coding: utf-8 -*-
{
    'name': "empresa_abogados",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.prueba_abogados_mayrin.com",
    "external_dependencies": {
        "python": ["python-docx"],
        "deb": ["libreoffice"],
    },
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','web'],

    # always loaded
    'data': [
         'views/views.xml',
        'views/vistas_cliente.xml',
        'views/vistas_licitacion.xml',
        'views/adjudicacion_form.xml',
        'views/acc_ventana.xml',
        'views/menu_item.xml',
        'report/certificado.xml',
        'report/facturas_arca_auditores.xml',
        'report/facturas_arca_consortium.xml',
        'views/proyecto_form.xml',
        'security/grupos_usuarios.xml',
        'security/ir.model.access.csv',
        'views/seguimiento_form.xml',
        'views/oferta_form.xml',
        'views/estudio_form.xml',
        'views/vistas_facturas.xml',
        'views/cliente_contactos_form.xml',
        'views/filtros.xml',
         'views/ficheros.xml',
         'views/calendario.xml'
    
    ],
    "qweb": [
    ],
   'web': {
        'assets_backend': {
            'xml': [
                'static/src/xml/qweb.xml',
            ],
        },
    },
   'installable': True,
    'auto_install': False,
    'application': True,
}