# -*- coding: utf-8 -*-
from odoo import fields, models, api


class CustomProduct(models.Model):
    _inherit = 'product.template'
    
    product_id = fields.Many2ona('product.mobile')


class ProductMobile(models.Model):
    _name = 'product.mobile'
    _description = 'Add manufacturer'

    manufacturer = fields.Selection([('huawei', 'Huawei')])


