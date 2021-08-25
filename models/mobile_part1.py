# -*- coding: utf-8 -*-
from odoo import fields, models, api


class CustomProduct(models.Model):
    _inherit = 'product.template'
    
    product_id = fields.Many2ona('mobile.phone')

class MobilePhone(models.Model):
    _name = 'mobile.phone'
    _inherit = 'product.template'
    _description = 'Add custom fields in product'

    manufacturer = fields.Selection([('huawei', 'Huawei')])
    model_phone = fields.Selection([('p20', 'P20')])
    
    @api.model
    def create(self, vals):
        print("Mobile phone create vals ",vals)
        return super(MobilePhone, self).create(vals)

    def write(self, vals):
        print("Mobile phone write vals ",vals)
        return super(MobilePhone, self).write(vals)

   
