# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ProductMobile(models.Model):
    _name = 'product.mobile'

    manufacturer = fields.Selection([('huawei', 'Huawei')])


