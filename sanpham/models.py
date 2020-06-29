from django.db import models
from django.template.defaultfilters import truncatechars
from PythonWeb.utils import get_unique_slug
import django_recommend
##
# Chọn sim vip _ thường
##

Default_img = '/default.png'

SIM_CHOICES = (
    ('khuyenmai', 'Khuyến Mãi'),
    ('thuong', 'Sim Thường'),
    ('vip', 'Sim Vip'),
    ('vipdn', 'Sim Vip Doanh Nhân'))

##
# Tạo danh muc san pham _Duc
##
class SimTheoGia(models.Model):
    title = models.CharField(max_length=100,verbose_name='Tiêu đề',unique=True)
    slug = models.SlugField(max_length=100, null=False, default='')

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Sim theo giá'


class NhaMang(models.Model):
    title = models.CharField(max_length=100,verbose_name='Tiêu đề',unique=True)
    slug = models.SlugField(max_length=100, null=False, default='')

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Nhà mạng'


class SimTheoLoai(models.Model):
    title = models.CharField(max_length=100,verbose_name='Tiêu đề')
    slug = models.SlugField(max_length=100, null=False, default='')

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Sim theo loại'


class SimNamSinh(models.Model):
    title = models.CharField(max_length=100,verbose_name='Tiêu đề')
    slug = models.SlugField(max_length=100, null=False, default='')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Sim năm sinh'


# Tạo bảng sản phẩm
class SanPham(models.Model):
    LoaiSims = models.ManyToManyField(SimTheoLoai,default=0, verbose_name='Loại sim')
    slug = models.SlugField(max_length=100, null=False, default='')
    luotxem = models.IntegerField(default=1)
    TacVu = models.CharField(max_length=100, choices=SIM_CHOICES,default='thuong',verbose_name='Tác vụ trang chủ')
    SoSim = models.CharField(max_length=100, verbose_name='Số sim',unique=True)
    Gia = models.IntegerField(verbose_name='Giá bán')
    Mang = models.ForeignKey(NhaMang, on_delete=models.CASCADE, null=True, verbose_name='Nhà Mạng')
    LoaiGia = models.ForeignKey(SimTheoGia, on_delete=models.CASCADE, null=True, verbose_name='Sim theo giá ')
    NamSinh = models.ForeignKey(SimNamSinh, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Theo năm sinh ')
    NgayNhap = models.DateTimeField(auto_now_add=True, verbose_name='Ngày nhập')
    DaBan = models.BooleanField(default=False, verbose_name='Đã bán')

    def __str__(self):
        return self.SoSim

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'SoSim', 'slug')
        super().save(*args, **kwargs)

    def get_loaisims(self):
        return " - ".join([s.title for s in self.LoaiSims.all()])

    def mark_viewed_by(self, user):

        """Record that the given Django user viewed this quote."""
        django_recommend.setdefault_score(user, self, 1)

    def mark_viewed_by_anonymous(self, session_key):
        """Record a non-authenticated user viewed this quote."""
        django_recommend.setdefault_score(session_key, self, 1)

    get_loaisims.short_description = "Loại sim"
    class Meta:
        verbose_name_plural = 'Sản Phẩm'


