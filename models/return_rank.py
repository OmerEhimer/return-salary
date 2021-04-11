# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _
from datetime import timedelta

class ReturnUnit(models.Model):
    _name = 'return.unit'
    _description = "unit"
    _rec_name = "unit_name"

    unit_name = fields.Char(string="Unit Name", required=True,)
