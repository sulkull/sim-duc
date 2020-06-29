from django.contrib import admin
from .models import DauGia

# Register your models here.
class DauGiaAdmin(admin.ModelAdmin):
    list_display = ['Sim', 'NgayHetHan', 'GiaMuaLuon', 'GiaHienTai', 'NguoiDauGiaHienTai', 'DaDauGia', 'DuongDan', 'id']
    search_fields = ['Sim']
    list_per_page = 5
    exclude = ['DuongDan']

admin.site.register(DauGia, DauGiaAdmin)