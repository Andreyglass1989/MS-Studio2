# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from projects_home.models import Rozdel


class Interer( models.Model ):
    class Meta:
        verbose_name = "ДИЗАЙН ИНТЕРЬЕРА"
        verbose_name_plural = "дизайны интерьеров"
    name = models.TextField(verbose_name=u'Название итерьера', max_length=255, help_text='имя интерьера')
    location = models.CharField(verbose_name=u'Местоположение', max_length=255)
    name_rozdela = models.ForeignKey(Rozdel, verbose_name=u'Имя раздела')
    image = models.ImageField(upload_to='design_interera')

    def __unicode__(self):
        return self.name + ' ' + self.location

    def image_img(self):
        if self.image:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100" /></a>'.format(self.image.url)
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True

class Gallery_design_interera (models.Model):
    class Meta:
        verbose_name = "ГАЛЕРЕЮ ДИЗАЙНА ИНТЕРЬЕРА"
        verbose_name_plural = "Галерея дизайна интерьеров"
    project = models.ForeignKey(Interer)
    img = models.ImageField(upload_to='design_interera')

    def project_name(self):
        return self.project

    def image_img(self):
        if self.img:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.img.url)
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True
