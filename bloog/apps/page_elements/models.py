from django.db import models


#################### MENUS ####################

LOCATIONS = (
        ('header',    'Header'),
        ('footer',    'Footer'),
        ('sideline',  'Sideline'),
    )

LINK_TYPES = (
        ('link',    'Link'),
        ('page',    'Page'),
    )


class Menu(models.Model):
    name = models.CharField(_('Menu'), max_length=40, blank=True, null=True)
    slug = models.SlugField()
    location = models.CharField(_('Menu Location'), max_length=30, choices=LOCATIONS)
    
    class Meta:
        verbose_name = _('Menu')
        verbose_name_plural = _('Menus')
    
    def __unicode__(self):
        pass
    
    def get_absolute_url(self):
        pass
    
    def main_items(self):
        return self.menuitem_set.filter(parent__isnull=True)


class MenuItem(models.Model):
    name = models.CharField(_('Name'), max_length=40)
    slug = models.SlugField(_('Slug'))
    menu = models.ForeignKey(Menu, verbose_name=_('Menu'))
    ordering = models.CharField(_('Ordering'), max_length=3)
    
    type = models.CharField(_('Link Type'), max_length=30, choices=LINK_TYPES)
    url = models.URLField(_('URL'))
    
    parent = models.ForeignKey('self', verbose_name=_('Parent'), blank=True, null=True)
    
    class Meta:
        verbose_name = _('Menu Item')
        verbose_name_plural = _('Menu Items')
        ordering = ('ordering',)
    
    def __unicode__(self):
        return "%s" % (self.name)
    
    def get_absolute_url(self):
        pass
    
    def _get_children(self):
        return MenuItem.objects.filter(parent=self)
    children = property(_get_children)
    
    def _has_children(self):
        return self.children.exists()
    has_children = property(_has_children)



#################### LINKS ####################

class LinkedPage(models.Model):
    name = models.CharField(max_length=30)
    url = models.URLField(_('URL'))
    ordering = models.CharField(_('Ordering'), max_length=40)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = _('Link')
        verbose_name_plural = _('Links')
        ordering = ('ordering',)
    
    def __unicode__(self):
        pass







