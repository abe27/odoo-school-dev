# -*- coding: utf-8 -*-

import uuid
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SchoolProfile(models.Model):
    _name = 'school.profile'
    _description = 'school.profile'

    first_name = fields.Char(string="ชื่อ",size=50, help="ระบุชื่อ", required=True)
    last_name = fields.Char(string="สกุล",size=50, help="ระบุสกุล", required=True)
    birth_date = fields.Date(string="วดป.เกิด", help="ระบุวดป.เกิด")
    email = fields.Char(index=True, string="Email Address", required=True)
    phone = fields.Char(string="Phone", default="-", help="ระบุหมายเลขโทรศัพท์")
    address = fields.Text(string="Address", default="-", help="ระบุที่อยู่")
    status = fields.Selection([('S', 'โสด'), ('M', 'สมรส'), ('N', 'ไม่เระบุ')], string="Status", help="สถานะภาพ", default="N")
    documents = fields.Binary(string="Documents", help="เอกสารประกอบ")
    document_name = fields.Char(string="Document Name")
    avatar_image = fields.Image(string="Avatar", max_width="300", max_height="300")
    is_active = fields.Boolean("Is Active", default=False)
    uuid_key = fields.Char(size=36,readonly=True, default=str(uuid.uuid4()))

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100

    @api.constrains('email')
    def _check_registration_no(self):
        for rec in self:
            domain = [('email', '=', rec.email)]
            count = self.sudo().search_count(domain)
            
            if count > 1:
                raise ValidationError(("The Email should be unique"))
