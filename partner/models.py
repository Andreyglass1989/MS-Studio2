# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Gallery(models.Model):
    img = models.ImageField(upload_to = 'partner')

    def image_img(self):
        if self.img:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.img.url)
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Партнеры логотип'
    image_img.allow_tags = True
