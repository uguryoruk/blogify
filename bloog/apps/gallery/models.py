from django.db import models


class Image(models.Model):
    name = models.CharField(_('Title'), max_length=30)
    image = models.ImageField(_('Image File'))
    ordering = models.CharField(max_length=3)

    class Meta:
        verbose_name = _('Picture')
        verbose_name_plural = _('Pictures')
        ordering = ('ordering',)
    
    def __unicode__(self):
        pass
    
    def get_absolute_url(self):
        pass


class Gallery(models.Model):
    name = models.CharField(_('Gallery Title'), max_length=30)
    slug = models.SlugField(_('Slug'))
    pictures = models.ManyToManyField(Image, verbose_name=_('Related Pictures'))
    description = models.CharField(_('Description'), max_length=150)

    class Meta:
        verbose_name = _('Galeri')
        verbose_name_plural = _('Galeriler')
        ordering = ('id',)
    
    def __unicode__(self):
        pass
    
    def get_absolute_url(self):
        pass