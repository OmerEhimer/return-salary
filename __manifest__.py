# -*- coding: utf-8 -*-
{
    'name': "Return Of Salary",
    'version' : '1.0',
    'sequence': 4,
    'description': 'This Mi First Project Return Of Salary',
    'category': 'Extra Tools',
    'summary':'Module For Return Of Salary',
    'website': 'https://www.Return-of-salary.com/',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    #update hajo Wad Ehimer
    # thi is our projact antar ffffffffffffffffffffffffff

    # any module necessary for this one to work correctly
    'depends': ['mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/return_rank.xml',
        'views/return_unit.xml',
        'views/type_of_return.xml',
        'views/return_employee.xml',

        'reports/report.xml',
        'reports/print_form_employee.xml',
        
        'wizards/wizard_print_return.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
