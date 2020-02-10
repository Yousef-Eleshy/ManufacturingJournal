# -*- coding: utf-8 -*-

from odoo import models, fields, api


class manufacturing_journal(models.TransientModel):
    _inherit = "res.config.settings"
    
    # Check Box - Enable Operation Expenses Account
    operation_expenses = fields.Boolean(string='Enable Operation Expenses Account', readonly=False)
    # Dropdown - Select Account
    account_selection = fields.Many2one('account.account', string='Operation Expenses Account')

    # Save Check Box Selection
    #Setter
    def set_values(self):
        super(manufacturing_journal, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param("operation_expenses", self.operation_expenses)
    #Getter
    @api.model
    def get_values(self):
        res = super(manufacturing_journal, self).get_values()
        params = self.env['ir.config_parameter'].sudo()
        operation_expenses = params.get_param('operation_expenses', default=False)
        res.update(operation_expenses=operation_expenses)
        return res
    
