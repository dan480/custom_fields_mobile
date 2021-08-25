# -*- coding: utf-8 -*-
from odoo import fields, models, api


class MobileProduct(models.Model):
    _name = 'mobile.product'
    
    #product_id = fields.Many2one('mobile.phone')
    manufacturer = fields.Selection([('huawei', 'Huawei')])
    #manufacturer = fields.One2many('custom.product', 'product_id')
    #model_phone = fields.Selection([('p20', 'P20')])
    

   
