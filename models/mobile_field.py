# -*- coding: utf-8 -*-
from odoo import fields, models, api

class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    #manufacturer_list = [('huawei', 'Huawei'), ('sony', 'Sony')]
    manufacturer = fields.Selection([('huawei', 'Huawei'), ('sony', 'Sony')])
    #model_list = {'huawei': [('p20', 'p20'), ('p30', 'p30')]}
    #model = fields.Selection(model_list.get(manufacturer))

    

