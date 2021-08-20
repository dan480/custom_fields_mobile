# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ProductMobile(models.Model):
    _name = "product.mobile"
    _inherit = "product.template"
    _description = "Add custom fields in Product Template"
    
    # custom fields
    manufacturer = fields.Selection([('huawei', 'Huawei'), ('xiaomi', 'Xiaomi'), ('samsung', 'Samsung'), ('sony', 'Sony')], string='Manufacturer')
    manufacturer_id = fields.Many2one('manufacturer', 'Manufacturer Id', index=True, ondelete='cascade')
    model = fields.One2many('product.mobile', 'manufacturer_id', 'Model')
