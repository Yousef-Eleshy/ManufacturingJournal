# -*- coding: utf-8 -*-

from odoo import models, fields, api


class manufacturing_journal(models.TransientModel):
     _inherit = "res.config.settings"
    
    _accounting_expenses = fields.Boolean(string='Use Operation Expenses', readonly=False)
    accounts_to_select = fields.Many2one('account.account',string= 'Choose operation Expenses Account')
    
    
    @api.model

    def set_values(self):

        super(ResConfigSettings, self).set_values()

        select_type = self.env['ir.config_parameter'].sudo()

        select_type.set_param('res.config.settings._accounting_expenses', self._accounting_expenses)



    @api.model

    def get_values(self):

        res = super(ResConfigSettings, self).get_values()

        select_type = self.env['ir.config_parameter'].sudo()

        sell = select_type.get_param('res.config.settings._accounting_expenses')

        res.update({ '_accounting_expenses' : sell})

        return res
    
    
    
        
    @api.model

    def set_values(self):

        super(ResConfigSettings, self).set_values()

        select_type = self.env['ir.config_parameter'].sudo()

        select_type.set_param('res.config.settings.accounts_to_select', self.accounts_to_select.id)
        
        
    
    
    @api.model

    def get_values(self):

        res = super(ResConfigSettings, self).get_values()

        select_type = self.env['ir.config_parameter'].sudo()

        sell = select_type.get_param('res.config.settings.accounts_to_select.id')

        res.update({ 'accounts_to_select' : int(sell)})

        return res