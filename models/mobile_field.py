# -*- coding: utf-8 -*-

from odoo import fields, models, api

class MobilePhone(models.Model):
    _name = "mobile.phone"
    _inherit = "product.template"
    
    # Relations fields    
    manufacturer_id = fields.Many2one('manufacturer', string='Manufacturer')
    model_id = fields.One2many('model', 'manufacturer_id', string='Model')
    manufacturer = fields.Char('Manufacturer')
    model = fields.Char('Model')
    
