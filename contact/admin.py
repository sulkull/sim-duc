from django.contrib import admin
from .models import LienHe
# Register your models here.
class LienHeAdmin(admin.ModelAdmin):
    list_display = ['id', 'HoTen', 'Email', 'SDT', 'TinNhan', 'Date']
    list_filter = ['Date']
    search_fields = ['HoTen']
    list_per_page = 10


admin.site.register(LienHe,LienHeAdmin)