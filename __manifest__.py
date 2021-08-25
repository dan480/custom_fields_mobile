# -*- coding: utf-8 -*-

{
    'name':'Custom_module',
    'version':'0.1',
    'author':'A.Sakovich',
    'summary':"Custom mobile module",
    'description':"A module that modifies the standard <Product> module",
    'category':'Customizations',
    'depends':['product'],
    'data': [
        'views/mobile_views_part1.xml',
        'views/mobile_views_part2.xml',
    ],
    'installable': True,

}
