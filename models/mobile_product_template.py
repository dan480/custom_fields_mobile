# -*- coding: utf-8 -*-

from odoo import fields, models

class ProductMobile(models.Model):
    _inherit = "product.template"
    _description = "Add custom fields in Product Template"
    
    # custom fields
    manufacturer = fields.Selection([('huawei', 'Huawei'),
                                     ('xiaomi', 'Xiaomi'),
                                     ('samsung', 'Samsung'),
                                     ('sony', 'Sony')],
                                    help="Please select manufacturer phone",
                                    )
