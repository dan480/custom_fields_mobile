# -*- coding: utf-8 -*-
from odoo import fields, models


class MobileProduct(models.Model):
    _inherit = 'product.template'
    
    #product_id = fields.Many2one('mobile.phone')
    manufacturer = fields.Selection([('huawei', 'Huawei')], string="Manufacturer")
    #manufacturer = fields.One2many('custom.product', 'product_id')
    model_phone = fields.Selection([('p20', 'P20')], string="Model")
    

   
