# -*- coding: utf-8 -*-
from odoo import fields, models, api


class CustomProduct(models.Model):
    _name = 'custom.product'
    _inherit = 'product.template'
    
    product_id = fields.Many2ona('mobile.phone')
    manufacturer = fields.Selection([('huawei', 'Huawei')])
    #manufacturer = fields.One2many('custom.product', 'product_id')
    #model_phone = fields.Selection([('p20', 'P20')])
   
