from django import template
from sanpham.models import SanPham

register = template.Library()
@register.simple_tag(name='category')
def get_meta():
    return SanPham.objects.filter(DaBan=False)