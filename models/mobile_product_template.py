# -*- coding: utf-8 -*-

from odoo import fields, models

class ProductMobile(models.Model):
    _inherit = "product.template"
    _description = "Add custom fields in Product Template"
    
    # custom field
    manufacturer = fields.Selection()
    manufaturer_id = fields.Many2one('product.template', string="Manufacturer")
    model_list = fields.One2many('product.template', 'manufaturer_id', string="Model list")
    model = fields.Selection(model_list)
    
