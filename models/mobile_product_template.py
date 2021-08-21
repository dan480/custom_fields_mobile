# -*- coding: utf-8 -*-

from odoo import fields, models

class ProductMobile(models.Model):
    _inherit = "product.template"
    _description = "Add custom fields in Product Template"
    
    # custom fields
    manufacturer = fields.Selection([('huawei', 'Huawei'), ('xiaomi', 'Xiaomi'), ('samsung', 'Samsung'), ('sony', 'Sony')], string='Manufacturer')
    manufacturer_id = fields.Many2one("manufacturer")
    model_list = {'huawei':['p20', 'p20 pro', 'p30', 'p30 pro']}     
    model = fields.One2many('model_list', 'manufacturer_id', 'Model')
