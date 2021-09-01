# -*- coding: utf-8 -*-
from odoo import fields, models, api


class MobileProduct(models.Model):
    _name = 'mobile.product'
    
    manufacturer_id = fields.Many2one('manufacturer.phone', string="Manufacturer")
    
class ManufacturerPhone(models.Model):
    _name = 'manufacturer.phone'
    
    manufacturer_name = fields.Char('Manufacturer')
    

#     @api.model
#     def create(self, values):
#         print("Student create method vals ", values)
#         rtn = super(MobileProduct, self).create(values)
#         return rtn

#     def write(self, values):
#         print("Student write method vals ", values)
#         rtn = super(MobileProduct, self).write(values)
#         return rtn

   
