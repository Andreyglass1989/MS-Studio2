# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Rozdel( models.Model ):
    name = models.CharField(verbose_name=u'Имя раздела', max_length=255)
    def __str__(self):
        return self.name


class Project( models.Model ):
    class Meta:
        verbose_name = "ПРОЕКТ ЖИЛОГО ДОМА"
        verbose_name_plural = "Проекты жилых домов"
    name = models.TextField(verbose_name=u'Имя проекта', max_length=255, help_text='название проекта')
    location = models.CharField(verbose_name=u'Местоположение', max_length=255)
    name_rozdela = models.ForeignKey(Rozdel, verbose_name=u'Имя проекта')
    image = models.ImageField(upload_to = 'projects_home')
    def __unicode__(self):
        return self.name + ' ' + self.location

    def image_img(self):
        if self.image:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url)
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True

class Gallery(models.Model):
    class Meta:
        verbose_name = "ГАЛЕРЕЮ ПРОЕКТА ЖИЛОГО ДОМА"
        verbose_name_plural = "Галерея проектов жилых домов"
    project = models.ForeignKey(Project)
    img = models.ImageField(upload_to = 'static/images/projects_home')

    def project_name(self):
        return self.project

    def image_img(self):
        if self.img:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.img.url)
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True



