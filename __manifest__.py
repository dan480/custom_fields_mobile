{
    'name':'Mobile_shop',
    'version':'1.1',
    'author':'A.Sakovich',
    'summary':"Online mobile phone shop",
    'sequence': 1,
    'description':"Store created on Odoo v13",
    'category':'Shop',
    'website':'null',
    'depends':['sale'],
    'data': [
        'views/assets.xml',
        'views/templates.xml',
        'views/sale_views.xml',
        'wizard/sale_product_configurator_views.xml',
    ],

}
