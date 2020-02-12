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


############# ATTEMPT 1 #############

    # Save Account Selection
    @api.onchange('account_selection')
    def save_account_selection(self):
        if self.account_selection:
            self.company_id.account_selection = self.account_selection
    

    
    
############# ATTEMPT 2 #############
    
#    def set_values(self):
#        res = super(manufacturing_journal, self).set_values()
#        self.env['ir.config_parameter'].set_param('manufacturing_journal.account_selection', self.account_selection)
#        return res
    
#    @api.model
#    def get_values(self):
#        res = super(manufacturing_journal, self).get_values()
#        ICPSudo = self.env['ir.config_parameter'].sudo()
#        selection = ICPSudo.get_param('manufacturing_journal.account_selection')
#        res.update(account_selection=selection)
#        return res




############# ATTEMPT 3 #############
        
#@api.model
#    def get_values(self):
#        res = super(manufacturing_journal, self).get_values()
#        res.update(
#            account_selection = self.env['ir.config_parameter'].sudo().get_param('manufacturing_journal.account_selection')
#        )
#        return res

    
#    def set_values(self):
#        super(manufacturing_journal, self).set_values()
#        param = self.env['ir.config_parameter'].sudo()

#        field1 = self.account_selection and self.account_selection.id or False

#        param.set_param('manufacturing_journal.account_selection', field1)


class ResCompany(models.Model):
    _inherit = "res.company"
    
     # Dropdown - Select Account
    account_selection = fields.Many2one('account.account', string='Operation Expenses Account')
    
    # Save Account Selection
    @api.onchange('account_selection')
    def save_account_selection(self):
        if self.account_selection:
            self.company_id.account_selection = self.account_selection
            
    
    