from django.contrib import admin
from .models import SanPham, SimNamSinh, SimTheoGia, SimTheoLoai, NhaMang
from import_export import resources, fields, widgets
from import_export.admin import ImportExportModelAdmin, ExportActionMixin


# Register your models here.


################--Xuất nhập khẩu--#######################

class Sim_Key(resources.ModelResource):
    class Meta:
        skip_unchanged = True
        report_skipped = True
        model = SanPham
        exclude = ['NgayNhap', 'slug', ]
        import_preview = (
            'id', 'LoaiSims__title', 'slug', 'TacVu', 'SoSim', 'Gia', 'Mang__title', 'LoaiGia__title', 'NamSinh',
            'Anh',)
        fields = (
        'id', 'LoaiSims', 'slug', 'TacVu', 'SoSim', 'Gia', 'Mang', 'LoaiGia', 'NamSinh',
        'Anh',)
    
    def before_import_row(self, row, **kwargs):
        if 'LoaiGia' in row:
            if row['LoaiGia'] == '':
                gia = int(row['Gia'])
                if gia < 500000:
                    loaigia_obj, created = SimTheoGia.objects.get_or_create(title="Sim dưới 500 nghìn")
                    row['LoaiGia'] = loaigia_obj.id
                elif gia >= 500000 and gia < 1000000:
                    loaigia_obj, created = SimTheoGia.objects.get_or_create(title="Sim giá 500 nghìn - 1 triệu")
                    row['LoaiGia'] = loaigia_obj.id
                elif gia >= 1000000 and gia < 3000000:
                    loaigia_obj, created = SimTheoGia.objects.get_or_create(title="Sim giá 1 triệu - 3 triệu")
                    row['LoaiGia'] = loaigia_obj.id
                elif gia >= 3000000 and gia < 5000000:
                    loaigia_obj, created = SimTheoGia.objects.get_or_create(title="Sim giá 3 triệu - 5 triệu")
                    row['LoaiGia'] = loaigia_obj.id
                elif gia >= 5000000 and gia < 10000000:
                    loaigia_obj, created = SimTheoGia.objects.get_or_create(title="Sim giá 5 triệu - 10 triệu")
                    row['LoaiGia'] = loaigia_obj.id
                elif gia >= 10000000 and gia < 50000000:
                    loaigia_obj, created = SimTheoGia.objects.get_or_create(title="Sim giá 10 triệu - 50 triệu")
                    row['LoaiGia'] = loaigia_obj.id
                elif gia >= 50000000 and gia < 100000000:
                    loaigia_obj, created = SimTheoGia.objects.get_or_create(title="Sim giá 50 triệu - 100 triệu")
                    row['LoaiGia'] = loaigia_obj.id
                elif gia >= 100000000:
                    loaigia_obj, created = SimTheoGia.objects.get_or_create(title="Sim giá trên 100 triệu")
                    row['LoaiGia'] = loaigia_obj.id
        return super(Sim_Key, self).before_import_row(row, **kwargs)


class Sim(ImportExportModelAdmin,ExportActionMixin):
    readonly_fields = ('LoaiGia',)
    list_display = ('SoSim', 'Gia', 'LoaiGia', 'Mang', 'TacVu', 'get_loaisims', 'NgayNhap', 'DaBan', 'id',)
    exclude = [ 'slug', ]
    list_per_page = 20
    resource_class = Sim_Key

    def save_model(self, request, obj, form, change):
        gia = obj.Gia
        print(gia)
        if gia < 500000:
            loaigia_obj, created = SimTheoGia.objects.get_or_create(title="Sim dưới 500 nghìn")
            obj.LoaiGia = loaigia_obj
        elif gia >= 500000 and gia < 1000000:
            loaigia_obj, created = SimTheoGia.objects.get_or_create(title="Sim giá 500 nghìn - 1 triệu")
            obj.LoaiGia = loaigia_obj
        elif gia >= 1000000 and gia < 3000000:
            loaigia_obj, created = SimTheoGia.objects.get_or_create(title="Sim giá 1 triệu - 3 triệu")
            obj.LoaiGia = loaigia_obj
        elif gia >= 3000000 and gia < 5000000:
            loaigia_obj, created = SimTheoGia.objects.get_or_create(title="Sim giá 3 triệu - 5 triệu")
            obj.LoaiGia = loaigia_obj
        elif gia >= 5000000 and gia < 10000000:
            loaigia_obj, created = SimTheoGia.objects.get_or_create(title="Sim giá 5 triệu - 10 triệu")
            obj.LoaiGia = loaigia_obj
        elif gia >= 10000000 and gia < 50000000:
            loaigia_obj, created = SimTheoGia.objects.get_or_create(title="Sim giá 10 triệu - 50 triệu")
            obj.LoaiGia = loaigia_obj
        elif gia >= 50000000 and gia < 100000000:
            loaigia_obj, created = SimTheoGia.objects.get_or_create(title="Sim giá 50 triệu - 100 triệu")
            obj.LoaiGia = loaigia_obj
        elif gia >= 100000000:
            loaigia_obj, created = SimTheoGia.objects.get_or_create(title="Sim giá trên 100 triệu")
            obj.LoaiGia = loaigia_obj
        obj.save()

admin.site.register(SanPham, Sim)


# Hiển thị bảng nhà mạng
class NhaMangAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'slug']
    search_fields = ['title']
    exclude = ['slug', ]
    list_per_page = 5


# Hiển thị bảng Sim theo loại
class LoaiSimResource(resources.ModelResource):
    class Meta:
        model = SimTheoLoai
        exclude = ('slug')
        fields = ('id', 'title')

class LoaiSimAdmin(ImportExportModelAdmin):
    list_per_page = 5
    exclude = [ 'slug', ]
    resource_class = LoaiSimResource


admin.site.register(SimTheoLoai, LoaiSimAdmin)


# Hiển thị bảng Sim theo giá
class SimTheoGiaAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'slug')
    exclude = ('slug',)
    search_fields = ['title']
    list_per_page = 5


# Hiển thị bảng Sim theo năm
# Hiển thị bảng Sim theo loại
class SimNamSinhResource(resources.ModelResource):
    class Meta:
        model = SimNamSinh
        exclude = ('slug')
        fields = ('id', 'title')
class SimTheoNamAdmin(ImportExportModelAdmin):
    list_per_page = 5
    exclude = [ 'slug', ]
    resource_class = SimNamSinhResource

admin.site.register(NhaMang, NhaMangAdmin)
admin.site.register(SimTheoGia, SimTheoGiaAdmin)
admin.site.register(SimNamSinh, SimTheoNamAdmin)
