# -*- coding: utf-8 -*-
from odoo import fields, models, api


class MobileProduct(models.Model):
    _inherit = 'product.template'

    mobile_name = fields.Char(dafault="Mobile phone", readonly=True, compute ='_compute_name')
    manufacturer_id = fields.Many2one('manufacturer.phone')
    manufacturer_name = fields.Char(string="Manufacturer", store=True, related="manufacturer_id.name")
    model_id = fields.Many2one('model.phone')
    model_name = fields.Char(string="Model", store=True, related="model_id.name")

    @api.model
    def create(self, values):
        new_record = super(MobileProduct, self).create(values)
        return new_record

    def write(self, values):
        res = super(MobileProduct, self).write(values)
        return res
    
    @api.onchange('manufacturer_id')
    def _manufacturer_onchange(self):
        res = {}
        res['domain']={'model_id':[('manufacturer_id', '=', self.manufacturer_id.id)]}
        return res
    
    @api.depends('manufacturer_name', 'model_name')
    def _compute_name(self):
        for rec in self:
            rec.mobile_name = "Mobile phone " + record.manufacturer_name + record.model_name


class ManufacturerPhone(models.Model):
    _name = 'manufacturer.phone'

    name = fields.Char('Manufacturer')
    rel_model = fields.One2many('product.template', 'model_id', 'Model')
    
    
class ModelPhone(models.Model):
    _name = 'model.phone'

    name = fields.Char('Model')



