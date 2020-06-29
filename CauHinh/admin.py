from django.contrib import admin

# Register your models here.
from CauHinh.models import CauHinhSeo, CauHinhTrang


class SEOAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']
    list_filter = ['title']
    search_fields = ['title']
    list_per_page = 10

    def has_add_permission(self, request):
        if CauHinhTrang.objects.filter(id=1):
            return False
        else:
            return True

    def has_delete_permission(self, request, obj=None):
        return False
admin.site.register(CauHinhSeo, SEOAdmin)

class SettingAdmin(admin.ModelAdmin):
     list_display = ['title', 'id']

admin.site.register(CauHinhTrang, SEOAdmin)
