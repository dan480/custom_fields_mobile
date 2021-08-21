# -*- coding: utf-8 -*-

from odoo import fields, models, api

class ProductMobile(models.Model):
    _name = "product.mobile"
    
    # Relations fields    
    manufacturer_id = fields.Many2one('manufacturer.phone', string='Manufacturer')
    model_id = fields.One2many('model.phone', 'manufacturer_id', string='Model')
    
class ManufacturerPhone(models.Model):
    _name = 'manufacturer.phone'
 
    manufacturer = fields.Char('Manufacturer')
    
class ModelPhone(models.Model):
    _name = 'model.phone'
 
    model = fields.Char('Model')
    
