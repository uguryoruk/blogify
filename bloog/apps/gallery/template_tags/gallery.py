from django import template
from picture_gallery.models import Gallery

register = template.Library()

@register.simple_tag(takes_context=True)
def display_gallery(context, gallery_name):
    """
    
    Template Usage:
    
        {% for picture in gallery %}
            {{ picture.image }}
            {{ picture.name }}
        {% endfor %}
    
    """
    try:
        gallery = Gallery.objects.get(name=gallery_name)
    except:
        gallery = None
    
    context['gallery'] = gallery
    
    return ""