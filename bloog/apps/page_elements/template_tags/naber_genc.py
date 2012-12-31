
from django import template
from page_elements.models import Menu, LinkedPage

register = template.Library()

@register.simple_tag(takes_context=True)
def get_menu(context, menu_name):
    """
        Return the Menu object for the given name
        
        Example:
        
        {% for item in menu.main_items %}
        
            {{ item }}
            
            {% if item.has_children %}
                {% for child in item.children %}
                    {{ child }}
                {% endfor %}
            {% endif %}
        
        {% endfor %}
        
    """
    try:
        menu = Menu.objects.get(name=menu_name)
    except:
        menu = None
    
    context['menu'] = menu
    
    return ""


@register.simple_tag(takes_context=True)
def get_links(context):
    """
        Return a list of active LinkedPage objects
        
        Example:
        
            {% for link in links %}
                <a href="{{ link.url }}">
                    {{ link.name }}
                </a>
            {% endfor %}
        
    """
    links = LinkedPage.objects.filter(is_active=True)
    
    context['links'] = links
    
    return ""


