# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


PAGE_TYPES = (
        ('homepage', u'Anasayfa'),
        ('postpage', u'Makale Sayfası'),
        ('all',      u'Tümü'), # diğerlerini pasif yapacak
    )


class SiteDetails(models.Model):
    about = models.TextField(_('About me'))    
    enable_comments = models.BooleanField(_('Enable comments'), default=True)


############ SEO ############


class SeoTemplate(models.Model):
    title = models.CharField(_('Title'), max_length=60)
    keywords = models.CharField(_('Keywords'))
    description = models.CharField(_('Description'))
    
    page = models.CharField(_('Page'), max_length=30, choices=PAGE_TYPES)
    
    class Meta:
        pass





