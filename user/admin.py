from typing import List
from django.contrib import admin
from .models import CustomerUser
# Register your models here.


class CustomerUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'GioiTinh', 'NgaySinh', 'SDT', 'DiaChi','id']
    search_fields = ['Username']
    list_per_page = 10


admin.site.register(CustomerUser, CustomerUserAdmin)
# admin.site.register(BinhLuanDanhGia, BinhLuanDanhGiaAdmin)