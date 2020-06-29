from django.db import models
from sanpham.models import SanPham
from user.models import CustomerUser
from PythonWeb.utils import get_unique_slug


# Create your models here.
class DauGia(models.Model):
    Sim = models.OneToOneField(SanPham, on_delete=models.CASCADE, verbose_name='Sim đấu giá', unique=True)
    NgayHetHan = models.DateTimeField(verbose_name='Ngày hết hạn')
    GiaMuaLuon = models.IntegerField(verbose_name='Giá mua luôn')
    GiaToiThieu = models.IntegerField(default=0, verbose_name='Giá tối thiểu')
    GiaHienTai = models.IntegerField(default=0, verbose_name='Giá hiện tại')
    NguoiDauGiaHienTai = models.ForeignKey(CustomerUser, on_delete=models.CASCADE, verbose_name='Người đấu giá hiện tại', null=True, blank= True)
    DuongDan = models.SlugField(max_length=100, null=False, default='')
    luotxem = models.IntegerField(default='1')
    DaDauGia = models.BooleanField(default=False, verbose_name='Đã đấu giá')

    def __str__(self):
        return self.Sim.SoSim
    
    def save(self, *args, **kwargs):
        if not self.DuongDan:
            self.DuongDan = get_unique_slug(self.Sim, 'SoSim', 'slug')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Đấu giá'