# -*- coding: utf-8 -*-

from odoo import fields, models

class ProductMobile(models.Model):
    _inherit = "product.template"
    _description = "Add custom fields in Product Template"
    
    # custom field
    manufacturer_list = [('huawei', 'Huawei'),
                         ('sony', 'Sony')]
    manufacturer = fields.Selection(selection_add(manufacturer_list),
                                    index=True,
                                    required=True)
    
    model_phone = fields.Selection([('p20', 'p20'), ('p20pro', 'p20pro')], stored=True, index=True, required=True)
    
