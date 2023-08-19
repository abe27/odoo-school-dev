# -*- coding: utf-8 -*-

import uuid
from odoo import models, fields, api


class SchoolProfile(models.Model):
    _name = 'school.profile'
    _description = 'school.profile'

    first_name = fields.Char(string="ชื่อ",size=50, help="ระบุชื่อ", required=True)
    last_name = fields.Char(string="สกุล",size=50, help="ระบุสกุล", required=True)
    birth_date = fields.Date(string="วดป.เกิด", help="ระบุวดป.เกิด")
    email = fields.Char(index=True, string="Email Address", required=True)
    phone = fields.Char(string="Phone", default="-", help="ระบุหมายเลขโทรศัพท์")
    address = fields.Text(string="Address", default="-", help="ระบุที่อยู่")
    is_active = fields.Boolean("Is Active", default=False)
    uuid_key = fields.Char(size=36,readonly=True, default=str(uuid.uuid4()))

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
