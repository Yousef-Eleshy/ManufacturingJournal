# -*- coding: utf-8 -*-

from odoo import models, fields, api


class manufacturing_journal(models.TransientModel):
    _inherit = "res.config.settings"
    
    operation_expenses = fields.Boolean(string='Enable Operation Expenses Account', readonly=False)
    account_selection = fields.Many2one('account.account',string= 'Operation Expenses Account')
    
    
   