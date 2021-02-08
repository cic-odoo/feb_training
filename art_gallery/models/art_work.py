# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import date

class ArtWork(models.Model):
    _name = 'art_gallery.art.work'
    _description = 'Art Work'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description', default='Art Work History')

    height = fields.Float(string='Height', required=True, default=1.0)
    width = fields.Float(string='Width', required=True, default=1.0)
    
    finished_date = fields.Date(string='Finished Date', default=date.today())
    
    product_id = fields.Many2one(comodel_name='product.template', string='Product')
    
    
