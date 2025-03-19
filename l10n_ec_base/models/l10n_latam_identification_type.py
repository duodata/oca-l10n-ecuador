# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class L10nLatamIdentificationType(models.Model):
    _inherit = 'l10n_latam.identification.type'

    code_ats_compra = fields.Char(string="Codigo ATS compra")
    code_ats_venta = fields.Char(string="Codigo ATS venta")
