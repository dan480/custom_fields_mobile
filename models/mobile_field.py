# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    name = fields.Char(default="Mobile phone", readonly=False)
    manufacturer = fields.Selection([('huawei', 'Huawei'), ('xiaomi', 'Xiaomi')])
    # manufacturer = fields.One2many('product.template', 'model_phone', string="Manufacturer", required=True)


class ModelPhone(models.Model):
    _inherit = 'product.template'

    model_phone = fields.Selection([('p20', 'P20'), ('p20pro', 'P20pro')])
    # model_phone = fields.Many2one('product_template', string="Model", required=True)


