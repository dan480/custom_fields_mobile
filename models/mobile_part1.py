# -*- coding: utf-8 -*-
from odoo import fields, models, api


class CustomProduct(models.Model):
    _inherit = 'product.template'
    
    product_id = fields.Many2ona('mobile.phone')
    manufacturer = fields.Selection([('huawei', 'Huawei')])
    #manufacturer = fields.One2many('custom.product', 'product_id')
    #model_phone = fields.Selection([('p20', 'P20')])
    
     @api.model
    def create(self , vals):
        # import pdb; pdb.set_trace()
        res = super(CustomProduct, self).create(vals)
        print("this function is working")
        return res
   
