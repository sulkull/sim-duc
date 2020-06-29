from typing import List
from django.contrib import admin
from .models import GioHang, CTGH
# Register your models here.

# Hiển thị giỏ hàng trên trang admin
class GioHangAdmin(admin.ModelAdmin):
    list_display = ['get_sanphams','id', 'user',  'TongTien']
    list_filter = ['id']
    search_fields = ['user']
    list_per_page = 10


# Hiển thị chi tiết giỏ hàng trên trang admin
class CTGHAdmin(admin.ModelAdmin):
    list_display = ['SP','id', 'GH',  'DonGia']
    list_filter = ['GH']
    search_fields = ['GH']
    list_per_page = 10


admin.site.register(GioHang, GioHangAdmin)
admin.site.register(CTGH, CTGHAdmin)
