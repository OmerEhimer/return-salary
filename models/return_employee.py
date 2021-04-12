# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
from datetime import timedelta

class ReturnEmployee(models.Model):
    _name = 'return.employee'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Return of Employee"
    _rec_name = "number_employee"

    number_employee = fields.Char(string="Number Employee", required=True,)
    name_employee = fields.Char(string="Name Employee", required=True,)
    rank_id = fields.Many2one('return.rank', string="Rank", required=True,)
    unit_id = fields.Many2one('return.unit', string="Unit", required=True,)
    return_line_ids = fields.One2many('return.employee.lines', 'form_id', string='line_ids')

class ReturnEmployeeLines(models.Model):
    _name = 'return.employee.lines'

    form_id = fields.Many2one('return.employee', string='Lines') 
    type_return = fields.Many2one('type.of.return', string="Type Of Return", required=True,)
    
    def year_selection(self):
            year = 2020 # replace 2000 with your a start year
            year_list = []
            while year != 2051: # replace 2030 with your end year
                  year_list.append((str(year), str(year)))
                  year += 1
            return year_list

    year = fields.Selection(
        year_selection,
        string="Year",
            default="2021", required=True # as a default value it would be 2019
        ) 

    month = fields.Selection([
        ('1', 'يناير'),
        ('2', 'فبراير'),
        ('3', 'مارس'),
        ('4', 'ابريل'),
        ('5', 'مايو'),
        ('6', 'يونيو'),
        ('7', 'يوليو'),
        ('8', 'أغسطس'),
        ('9', 'سبتمبر'),
        ('10', 'أكتوبر'),
        ('11', 'نوفمبر'),
        ('12', 'ديسمبر'),
        ('13', 'okay'),
     ], string="Month" , required=True)      

    return_salary = fields.Float(string='Amount', required=True, )
    status = fields.Selection([('1','لم يتم التسليم'),('2','تم التسليم')], string="Status", default='1',)
    notes = fields.Text(string='Notes',)

    def print_employee(self):
        print("Print Any")
