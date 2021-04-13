# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
from datetime import timedelta

class ReturnEmployee(models.Model):
    _name = 'return.employee'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Return of Employee"
    _rec_name = "number_employee"

    number_employee = fields.Char(string="Number Employee", required=True, track_visibility="always",)
    name_employee = fields.Char(string="Name Employee", required=True,  track_visibility="always",)
    rank_id = fields.Many2one('return.rank', string="Rank", required=True,  track_visibility="always",)
    unit_id = fields.Many2one('return.unit', string="Unit", required=True,  track_visibility="always",)
    return_line_ids = fields.One2many('return.employee.lines', 'form_id', string='line_ids',  track_visibility="always",)
    count_type_return_lines = fields.Integer(compute='get_count_type_line' , string="Count" ,  track_visibility="always",)  
    user_id = fields.Many2one('res.users',string="Resposible",readonly="1",default=lambda self:self.env.user)


    @api.multi
    def count_type_return(self):
        return {
            'name': _('Return'),
            'domain': [('form_id','=', self.ids)],
            'view_type': 'form',
            'res_model': 'return.employee.lines',
            'view_mode': '',
            # 'type': 'ir.actions.act_window',
        }

    @api.multi
    def get_count_type_line(self): 
        for rec in self:   
            count_type = rec.env['return.employee.lines'].search_count([('form_id','=', self.ids)])
            self.count_type_return_lines=count_type


class ReturnEmployeeLines(models.Model):
    _name = 'return.employee.lines'

    form_id = fields.Many2one('return.employee', string='Lines') 
    type_return = fields.Many2one('type.of.return', string="Type Of Return", required=True,  track_visibility="always",)
    
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
     ], string="Month" , required=True, track_visibility="always",)      

    return_salary = fields.Float(string='Amount', required=True, track_visibility="always",)
    status = fields.Selection([('1','لم يتم الصرف'),('2','تم الصرف  ')], string="Status", default='1',  track_visibility="always",)
    notes = fields.Text(string='Notes',  track_visibility="always",)
    date_cashing = fields.Date(string='Date Cashing', default=fields.Date.today(),  track_visibility="always",)
    reason_return = fields.Text(string='Reason Of Return', default='غياب', track_visibility="always")
    id_return = fields.Boolean()
    
    _sql_constraints = [
        (
            'constraint_uniq_name',
            'unique(form_id,type_return,year,month)',
            'لا يمكن حساب أكثر من مرتجع في نفس الشهر '
        ),
    ]  

    @api.multi
    def get_print(self):
            # data={
            # 'model':'return.employee.lines',
            # 'form':self.read()[0]
            # }
        return self.env.ref('return_salary.report_employee').report_action(self)    