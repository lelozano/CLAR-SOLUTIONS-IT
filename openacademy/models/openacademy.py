# -*- coding: utf-8 -*-

from odoo import models, fields, api


class openacademy(models.Model):
    _name = 'openacademy.openacademy'
    _description = 'Open Academy'

    name = fields.Char()
    # salud = fields.Float('Salud (%)', _compute='_compute_salud')
    # m2o = fields.Many2one('res.partner', 'Salud')
    # o2m = fields.One2many('res.partner', 'openacademy_id', 'Salud')
    # m2m = fields.Many2many('res.partner', 'partner_open_rel', 'open_id', 'partner_id', 'Salud')

class OpenacademyCourse(models.Model):
    _name = 'openacademy.course'
    _description = 'Open Academy Course'

    name = fields.Char()
    description = fields.Char('Description')