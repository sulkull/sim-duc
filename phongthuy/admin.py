from django.contrib import admin
# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from phongthuy.models import *


class ptResource(resources.ModelResource):
    class Meta:
        model = Datapt
# Hiển thị bảng Sim theo loại
class ptadmin(ImportExportModelAdmin):
    resource_class = ptResource
admin.site.register(Datapt, ptadmin)


class nguhanhGoc(resources.ModelResource):
    class Meta:
        model = nguhanh
# Hiển thị bảng Sim theo loại
class nguhanhadmin(ImportExportModelAdmin):
    resource_class = nguhanhGoc
admin.site.register(nguhanh, nguhanhadmin)


class namsinhGoc(resources.ModelResource):
    class Meta:
        model = namsinh
        fields = ('namsinh','nguhanh_ns')
# Hiển thị bảng Sim theo loại
class namsinhadmin(ImportExportModelAdmin):
    resource_class = namsinhGoc
admin.site.register(namsinh, namsinhadmin)