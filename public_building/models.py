# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from projects_home.models import Rozdel


class Building ( models.Model ):
    class Meta:
        verbose_name = "ПРОЕКТ ОБЩ. НАЗНАЧ."
        verbose_name_plural = "Проеты общественного назначения"
    name = models.TextField(verbose_name=u'Имя проекта', max_length=255, help_text='название проекта')
    location = models.CharField(verbose_name=u'Местоположение', max_length=255)
    name_rozdela = models.ForeignKey(Rozdel, verbose_name=u'Имя проекта')
    image = models.ImageField(upload_to = 'public_building')
    def __unicode__(self):
        return self.name + ' ' + self.location

    def image_img(self):
        if self.image:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url)
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True

class Gallery_building ( models.Model ):
    class Meta:
        verbose_name = "ГАЛЕРЕЮ ПР-ОВ ОБЩ. НАЗНАЧ."
        verbose_name_plural = "Галерия проетов общественного назначения"
    project = models.ForeignKey ( Building )
    img = models.ImageField ( upload_to = 'public_building' )

    def project_name(self):
        return self.project

    def image_img(self):
        if self.img:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.img.url)
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True