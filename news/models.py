from django.db import models
from PythonWeb.utils import get_unique_slug


# Create your models here.

#Tạo bảng danh mục tin tức
class DanhMucTinTuc(models.Model):
    TieuDe = models.CharField(max_length=500 ,null=True, verbose_name='Tên danh mục tin tức')
    DuongDan = models.SlugField(max_length=100, null=False, default='', verbose_name='Đường dẫn')

    def __str__(self):
        return self.TieuDe

    def save(self, *args, **kwargs):
        if not self.DuongDan:
            self.DuongDan = get_unique_slug(self, 'TieuDe', 'DuongDan')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Danh mục tin tức'

# Tạo bảng tin tức
class TinTuc(models.Model):
    LoaiTinTuc = models.ForeignKey(DanhMucTinTuc, on_delete=models.CASCADE, null=False, verbose_name='Danh mục tin tức')
    TieuDe = models.TextField(null=True, verbose_name='Tiêu đề')
    MoTaNgan = models.TextField(null=True, verbose_name='Mô tả ngắn')
    NoiDung = models.TextField(null=True, verbose_name='Nội dung')
    Anh = models.ImageField(default='product-default.jpg', verbose_name='Ảnh')
    NgayTao = models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')
    DuongDan = models.SlugField(max_length=200, null=False, default='', verbose_name='Đường dẫn')
    
    def __str__(self):
        return self.TieuDe

    def save(self, *args, **kwargs):
        if not self.DuongDan:
            self.DuongDan = get_unique_slug(self, 'TieuDe', 'DuongDan')
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'Tin tức'


