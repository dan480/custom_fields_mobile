# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _, SUPERUSER_ID

class MobileProduct(models.Model):
    _name = "mobile_product.template"
    _inherit = "product"
    _description = "Add custom fields in Product Template"
    
    # custom fields
    manufacturer = fields.One2many(
        'product.manufacturer', 'Manufacturer', required=True, help="Select manufacturer for the current product")
    #model = fields.One2one()
