# -*- coding: utf-8 -*-
from odoo import fields, models, api


class MobileProduct(models.Model):
    _inherit = 'product.template'

    name = fields.Char(dafault="Mobile phone", readonly=True, compute='_compute_name')
    manufacturer_id = fields.Many2one('manufacturer.phone', required=True)
    manufacturer_id_name = fields.Char(string="Manufacturer", related="manufacturer_id.name")
    model_id = fields.Many2one('model.phone', required=True)
    model_id_name = fields.Char(string="Model", related="model_id.name")

    @api.model
    def create(self, values):
        rec = super(MobileProduct, self).create(values)
        return rec

    def write(self, values):
        rec = super(MobileProduct, self).write(values)
        return rec

    @api.onchange('manufacturer_id')
    def onchange_manufacturer_id(self):
        res = {}
        res['domain'] = {'model_id': [('model_phone_id', '=', self.manufacturer_id.id)]}
        return res

    @api.depends('manufacturer_id_name', 'model_id_name')
    def _compute_name(self):
        for rec in self:
            if rec.manufacturer_id_name or rec.model_id_name:
                rec.name = "Mobile phone " + str(rec.manufacturer_id_name) + ' ' + str(rec.model_id_name)
            else:
                rec.name = "Mobile phone"


class ManufacturerPhone(models.Model):
    _name = 'manufacturer.phone'

    name = fields.Char(string="Manufacturer")
    model_ids = fields.One2many('model.phone', 'model_phone_id', string="Manufacturer")


class ModelPhone(models.Model):
    _name = 'model.phone'

    name = fields.Char(string="Model")
    model_phone_id = fields.Many2one('manufacturer.phone', string="Model", required=True)
