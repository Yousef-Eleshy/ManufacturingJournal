# -*- coding: utf-8 -*-

from odoo import models, fields, api


class manufacturing_journal(models.TransientModel):
    _inherit = "res.config.settings"
    
    _accounting_expenses = fields.Boolean(string='Enable Operation Expenses Account', readonly=False)
    accounts_to_select = fields.Many2one('account.account',string= 'Operation Expenses Account')
    
    
   