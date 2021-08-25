# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ProductMobile(models.Model):
    _inherit = 'product.template'

    product_name = fields.Char(default="Mobile phone", readonly=True)
    manufacturer = fields.One2many('product.template', 'product_name')
    model_phone = fields.Many2one('product.template', index=True, ondelete='cascade')

    @api.model
    def create(self, values):
        print("Product create method vals ", values)
        rtn = super(product.template, self).create(values)
        return rtn

    def write(self, values):
        print("Student write method vals ", values)
        rtn = super(product.template, self).write(values)
        return rtn

    @api.constrains('parent_id')
    def _check_category_recursion(self):
        if not self._check_recursion():
            raise ValidationError(_('You cannot create recursive categories.'))
        return True

    @api.model
    def name_create(self, name):
        return self.create({'name': name}).name_get()[0]

    def unlink(self):
        main_category = self.env.ref('product.product_category_all')
        if main_category in self:
            raise UserError(_("You cannot delete this product category, it is the default generic category."))
        return super().unlink()
    # def specialCommand(self):
        # Below code is only for 0,0,vals command

        # First Way to create child model for existing parent model.
        # student_obj = self.env['school.student']
        # stud_id = student_obj.create({'name':"Student ONE", 'school_id':self.id})

        # Parent model and child model.
        # school_id = self.create({"name":"Kapil Sharma Show"})
        # student_obj.create({"name":"Kapil Student 1", "school_id":school_id.id})
        # student_obj.create({"name":"Kapil Student 2", "school_id":school_id.id})
        # student_obj.create({"name":"Kapil Student 3", "school_id":school_id.id})
        # student_obj.create({"name":"Kapil Student 4", "school_id":school_id.id})
        # student_obj.create({"name":"Kapil Student 5", "school_id":school_id.id})

        # Using speicial Command
        # self.create({"name": "Babita School", "school_list": [(0, 0, {'name': "Babita Student 1", "total_fees": 300}),
        #                                                       (0, 0, {'name': "Babita Student 2", "total_fees": 400}),
        #                                                       (0, 0, {'name': "Babita Student 3", "total_fees": 500}),
        #                                                       (0, 0, {'name': "Babita Student 4", "total_fees": 700}),
        #                                                       (0, 0, {'name': "Babita Student 5", "total_fees": 800})]})
        # # self.write({"school_list": [[0,0,{'name':'Babita School 6'}]]})
        # pass








