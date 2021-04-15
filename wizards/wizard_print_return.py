# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
from datetime import timedelta

class WizardPrintReturnEmployee(models.TransientModel):
      _name = 'print.return.employee'

      number_employee = fields.Char(string="Number Employee", related='active_return_emp_id.number_employee', required=True,)
      name_employee = fields.Char(string="Name Employee",related='active_return_emp_id.name_employee', required=True,)
      rank_id = fields.Many2one('return.rank', string="Rank", related='active_return_emp_id.rank_id', required=True,)
      unit_id = fields.Many2one('return.unit', string="Unit", related='active_return_emp_id.unit_id', required=True,)
      return_line_ids = fields.One2many('print.return.lines', 'form_id', string='line_ids',)
      active_return_emp_id = fields.Many2one('return.employee', string="Active Id") 

      @api.onchange('active_return_emp_id')
      def on_change(self):
            # print(">>>>>>>>>>>>>>>>" , self.active_return_emp_id)
            lines = []
            for rec in self.active_return_emp_id.return_line_ids:
                  if rec.id_return==False:
                        print()
                        vals = (0,0,{'active_return_lines_id' : rec.id})
                        lines.append(vals)
            return {
                  'value' : {
                        'return_line_ids' : lines,
                        }                                  
            }


class WizardPrintReturnlines(models.TransientModel):
      _name = 'print.return.lines'
      
      form_id = fields.Many2one('print.return.employee', string='Lines') 
      type_return = fields.Many2one(string='Return Type', related='active_return_lines_id.type_return',)
      return_salary = fields.Float(string='Amount', related='active_return_lines_id.return_salary',)
      
      status = fields.Selection([('1','لم يتم الصرف'),('2','تم الصرف  ')], string="Status", related='active_return_lines_id.status',)
      notes = fields.Text(string='Notes', related='active_return_lines_id.notes',)
      date_cashing = fields.Date(string='Date Cashing', default=fields.Date.today(),related='active_return_lines_id.date_cashing',)
      reason_return = fields.Text(string='Reason Of Return', default='غياب',related='active_return_lines_id.reason_return',)
      active_return_lines_id = fields.Many2one('return.employee.lines', string="Active Id Lines") 
      id_return = fields.Boolean()

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
      , related='active_return_lines_id.year',) 

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
      ], string="Month" , related='active_return_lines_id.month',)  

      

