# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Gallery(models.Model):
    class Meta:
        verbose_name = "ЛОГОТИП ПАРТНЕРОВ"
        verbose_name_plural = "Логотипы партнеров"
    img = models.ImageField(upload_to = 'partner', verbose_name="картинка/логотип")
    link = models.CharField(max_length=255, verbose_name="ссылка")

    def image_img(self):
        if self.img:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.img.url)
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Партнеры логотип'
    image_img.allow_tags = True
