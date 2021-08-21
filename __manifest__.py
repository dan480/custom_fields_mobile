# -*- coding: utf-8 -*-

{
    'name':'Custom_module',
    'version':'1.1',
    'author':'A.Sakovich',
    'summary':"Custom mobile module",
    'description':"Module for creating a product-mobile phone",
    'category':'Customizations',
    'depends':['base', 'sale'],
    'data': [
        'views/product_template_views.xml',
        'views/add_phone_menu.xml',
        'views/add_quick_create.xml',
    ],
    'installable': True

}
