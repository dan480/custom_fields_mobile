# -*- coding: utf-8 -*-

from odoo import fields, models, api

class MobilePhone(models.Model):
    _name = "mobile.phone"
    
    manufacturer_list = [('huawei', 'Huawei'), ('sony', 'Sony')]
    manufacturer = fields.Selection(manufacturer_list)
    model_list = {'huawei': [('p20', 'p20'), ('p30', 'p30')]}
    model = fields.Selection(model_list.get(manufacturer))
    
