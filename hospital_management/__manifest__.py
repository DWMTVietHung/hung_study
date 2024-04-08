# -*- coding: utf-8 -*-
{
    'name': "hospital_management",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'sequence': -1,

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'application': True,
    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        'security/group.xml',
        'security/ir.model.access.csv',
        'views/menu_item.xml',
        'views/hospital_nurse.xml',
        'views/hospital_patient.xml',
        'views/hospital_doctor.xml',
        'views/inherit_sale_order.xml',
        'views/res_config_settings_views.xml',
        'views/inherit_hrm_employee.xml',
        'views/medicine.xml',


    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}
