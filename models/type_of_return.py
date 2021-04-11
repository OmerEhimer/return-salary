# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _
from datetime import timedelta

class TypeOfReturn(models.Model):
    _name = 'type.of.return'
    _description = "type of return"

    type_return_name = fields.Char(string="Type Of Return", required=True,)
  