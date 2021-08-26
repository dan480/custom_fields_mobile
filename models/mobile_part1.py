# -*- coding: utf-8 -*-
from odoo import fields, models, api


class MobileProduct(models.Model):
    _inherit = 'product.template'
    _rec_name = 'name_manufacturer'

    name_manufacturer = fields.Char('manufacturer')
    manufacturer = fields.Many2one('product.template', string="Manufacturer")
    # model = fields.One2many('product.template', 'manufacturer', string="Model")

    @api.model
    def create(self, values):
        print("Student create method vals ", values)
        rtn = super(MobileProduct, self).create(values)
        return rtn

    # No Decorator
    def write(self, values):
        print("Student write method vals ", values)
        rtn = super(MobileProduct, self).write(values)
        return rtn











    

   
