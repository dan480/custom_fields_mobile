# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _, SUPERUSER_ID

class MobileProduct(models.Model):
    _name = "mobile_product.template"
    _inherit = "product"
    _description = "Add custom fields in Product Template"
    
    # custom fields
    manufacturer = fields.Selection([('huawei', 'Huawei'), ('xiaomi', 'Xiaomi'), ('samsung', 'Samsung'), ('sony', 'Sony')], string='Manufacturer')
    # model = fields.One2Many()
