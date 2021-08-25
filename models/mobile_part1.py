# -*- coding: utf-8 -*-
from odoo import fields, models, api


class CustomProduct(models.Model):
    _inherit = 'product.template'
    
    product_id = fields.Many2ona('manufacturer.phone')
    manufacturer = fields.Selection([('huawei', 'Huawei')])


class ManufacturerPhone(models.Model):
    _name = 'manufacturer.phone'
    _description = 'Add field manufacturer in product'

    manufacturer = fields.Selection([('huawei', 'Huawei')])

class ModelPhone(models.Model):
    _name = 'model.phone'
    _description = 'Add field model in product'
    
    model_phone = fields.Selection([('p20', 'P20')])

