# -*- coding: utf-8 -*-

from odoo import fields, models, api

class MobilePhone(models.Model):
    _inherit = "product.template"
    
    # Relations fields    
    manufacturer_id = fields.Char('Manufacturer')
    #model_id = fields.One2many('model_phone', 'manufacturer_id', string='Model')
    manufacturer = fields.Char('Manufacturer')
    model = fields.Char('Model')
    
