from django.contrib import admin
from .models import TinTuc,DanhMucTinTuc
from django.utils.safestring import mark_safe

# Register your models here.
class TinTucAdmin(admin.ModelAdmin):
    list_display = [ 'TieuDe', 'MoTaNgan', 'Anh', 'NgayTao', 'DuongDan', 'LoaiTinTuc', 'id']
    list_filter = ['NgayTao']
    search_fields = ['TieuDe']
    exclude = ['DuongDan', ]
    list_per_page = 5

    class Media:
        js = ('tinymce/tinymce.min.js', 'home/js/tinymce_4_config.js')

    def _Noi_dung(self, obj):
        _NoiDung = mark_safe(obj.NoiDung)
        return _NoiDung


admin.site.register(TinTuc,TinTucAdmin)


class DanhMucTinTucAdmin(admin.ModelAdmin):
    list_display = [ 'TieuDe', 'DuongDan', 'id']
    search_fields = ['TieuDe']
    exclude = ['DuongDan', ]
    list_per_page = 5


admin.site.register(DanhMucTinTuc,DanhMucTinTucAdmin)
