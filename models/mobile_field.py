# -*- coding: utf-8 -*-

from odoo import fields, models, api

class MobilePhone(models.Model):
    _inherit = "product.template"
    
    # Relations fields    
    
    manufacturer = fields.Char()
    model = fields.Char()
    
