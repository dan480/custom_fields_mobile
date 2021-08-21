# -*- coding: utf-8 -*-

{
    'name':'Custom_module',
    'version':'0.1',
    'author':'A.Sakovich',
    'summary':"Custom mobile module",
    'description':"Module for creating a product-mobile phone",
    'category':'Customizations',
    'depends':['base', 'sale', 'product'],
    'data': [
        'views/product_template_views.xml',
        'views/add_phone_menu.xml',
        'views/add_quick_create.xml'
    ],
    'installable': True

}
