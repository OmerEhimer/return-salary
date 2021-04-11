# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _
from datetime import timedelta

class ReturnRank(models.Model):
    _name = 'return.rank'
    _description = "rank"
    _rec_name = "rank_name"

    rank_name = fields.Char(string="Rank Name", required=True,)
    rank_type = fields.Selection(
        [('1', 'ضابط'),
         ('2','ضابط صف'), 
         ('3','متعاقد')] 
         , string="Rank Type", required=True)
    rank_number = fields.Integer(string="Number Of Rank", required=True,)