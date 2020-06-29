from django.db import models
from giohang.models import GioHang, CTGH
from user.models import CustomerUser
from django.db.models.signals import pre_save, post_save


# Create your models here.
class HoaDon(models.Model):
    GH = models.ForeignKey(GioHang, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Giỏ hàng')
    HoTenNguoiNhan = models.CharField(default='', max_length=200, verbose_name='Họ tên người nhận')
    DiaChiNguoiNhan = models.TextField(default='', verbose_name='Địa chỉ người nhận')
    SDT = models.CharField(default='', max_length=10, verbose_name='Số điện thoại người nhận')
    NgayDatHang = models.DateTimeField(auto_now_add=True, verbose_name='Ngày đặt hàng')
    ThanhToan = models.BooleanField(default=False, verbose_name='Thanh toán')
    GiaoHang = models.BooleanField(default=False, verbose_name='Giao hàng')
    TongTien = models.IntegerField(default=0, verbose_name='Tổng tiền')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.HoaDon = None

    def __str__(self):
        return str(self.id)

    def update_total(self):
        cart_total = self.GH.TongTien
        self.TongTien = cart_total
        self.save()
        return cart_total

    def check_done(self):
        #Kiểm tra thông tin user
        user = CustomerUser.objects.get(id=self.GH.user.id)
        tongtien = self.TongTien
        if self.HoTenNguoiNhan and self.DiaChiNguoiNhan and self.SDT and user.email and tongtien > 0:
            return True
        return False

    @property
    def hidden_phone_number(self):
        return '%sxxxx%s' % (self.SDT[:3], self.SDT[-3:])

    class Meta:
        verbose_name_plural = 'Hóa đơn'


def post_save_cart_total(sender, instance, created, *args, **kwargs):
    if not created:
        cart_obj = instance
        qs = HoaDon.objects.filter(GH=cart_obj)
        if qs.count() == 1:
            order_obj = qs.first()
            order_obj.update_total()


post_save.connect(post_save_cart_total, sender=GioHang)


def post_save_order(sender, instance, created, *args, **kwargs):
    if created:
        instance.update_total()


post_save.connect(post_save_order, sender=HoaDon)