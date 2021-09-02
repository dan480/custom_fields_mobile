# -*- coding: utf-8 -*-
from odoo import fields, models, api


class MobileProduct(models.Model):
    _inherit = 'product.template'

    manufacturer_id = fields.Many2one('manufacturer.phone')
    manufacturer_name = fields.Char(string="Manufacturer", store=True, related="manufacturer_id.name")
    model_id = fields.Many2one('model.phone')
    model_name = fields.Char(string="Model", store=True, related="model_id.name")

    @api.model
    def create(self, values):
        new_record = super(MobileProduct, self).create(values)
        return new_record

    def write(self, values):
        rtn = super(MobileProduct, self).write(values)
        return rtn


class ManufacturerPhone(models.Model):
    _name = 'manufacturer.phone'

    name = fields.Char('Manufacturer')
    
    
class ModelPhone(models.Model):
    _name = 'model.phone'

    name = fields.Char('Model')



