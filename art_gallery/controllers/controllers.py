# -*- coding: utf-8 -*-
from odoo import http


class ArtGallery(http.Controller):
    @http.route('/art_gallery/art_gallery/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/art_gallery/', auth='public')
    def list(self, **kw):
        art = http.request.env['art_gallery.art.work'].search([])
        return http.request.render('art_gallery.art_gallery_web', {'art': art})

#     @http.route('/art_gallery/art_gallery/objects/<model("art_gallery.art_gallery"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('art_gallery.object', {
#             'object': obj
#         })
