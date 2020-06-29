from django import template
from news.models import TinTuc

register = template.Library()
@register.simple_tag(name='tintuc')
def get_meta():
    return TinTuc.objects.all()