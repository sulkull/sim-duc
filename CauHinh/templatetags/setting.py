import re
from django import template
from CauHinh.models import CauHinhTrang

register = template.Library()
@register.simple_tag(name='setting')
def get_meta():
    return CauHinhTrang.objects.all()