# -*- coding: utf-8 -*-

from odoo import models, fields, api


class manufacturing_journal(models.Model):
    _inherit = "stock.location"
    
    # Dropdown - Select Account
    account_selection = fields.Many2one('account.account', string='Operation Expenses Account')

