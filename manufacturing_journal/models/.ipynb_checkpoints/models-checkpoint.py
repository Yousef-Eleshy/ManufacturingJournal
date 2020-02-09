# -*- coding: utf-8 -*-

from odoo import models, fields, api


class manufacturing_journal(models.TransientModel):
    _inherit = "res.config.settings"
    
    _accounting_expenses = fields.Boolean(string='Use Operation Expenses', readonly=False)
    accounts_to_select = fields.Many2one('account.account',string= 'Choose operation Expenses Account')
    
    
   