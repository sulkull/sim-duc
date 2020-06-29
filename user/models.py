import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from sanpham.models import SanPham


# Create your models here.
class CustomerUser(AbstractUser):
    SDT = models.CharField(default='', max_length=10, verbose_name='Số điện thoại')
    DiaChi = models.TextField(default='', verbose_name='Địa chỉ')
    choices = [('0', 'Nam'), ('1', 'Nữ'), ('2', 'Không xác định')]
    GioiTinh = models.CharField(choices=choices, default='2', max_length=20, verbose_name='Giới tính')
    NgaySinh = models.DateField(null=True, verbose_name='Ngày sinh')

    def HoTen(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name_plural = 'Người dùng'


