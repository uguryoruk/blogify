# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from django.contrib.markup.templatetags import markup
from django.template.defaultfilters import slugify


class Tag(models.Model):
    name = models.CharField(_('Tag name'), max_length=25)
    slug = models.SlugField(_('Slug'), unique=True)
    
    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')
        ordering = ('-name',)
    
    def save(self, *args, **kwargs):
        self.name = self.name.strip().lower()
        # geçici çözüm...kendi slugify'ını olustur
        if not self.slug:
            self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        pass


class PostManager(models.Manager):
    def active_posts(self):
        return self.filter(is_active=True)


class Post(models.Model):
    title = models.CharField(_('Title'), max_length=70)
    slug = models.SlugField(_('Slug'))
    
    content = models.TextField(_('Content'))
    rendered_content = models.TextField(_('Rendered content'), blank=True)
    
    author = models.ForeignKey(User, verbose_name=_('Author'))
    
    date_created = models.DateTimeField(_('Date created'), default=datetime.now)
    date_modified = models.DateTimeField(_('Date modified'))
    
    is_active = models.BooleanField(_('Is active'), default=False)
    
    tags = models.ManyToManyField(Tag, verbose_name=_('Tags'), blank=True)
    
    objects = PostManager()
    
    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ('-date_created',)
    
    def save(self, *args, **kwargs):
        self.last_edited_at = datetime.now()
        self.rendered_content = markup.markdown(self.content)
        if not self.author:
            pass
        super(Post, self).save(*args, **kwargs)
    
    def __unicode__(self):
        pass
    
    def get_absolute_url(self):
        pass






