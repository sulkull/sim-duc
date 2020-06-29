from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from sanpham.models import SimTheoLoai, SimNamSinh, NhaMang, SimTheoGia
from news.models import TinTuc, DanhMucTinTuc
import operator


app_name = 'user'
urlpatterns = [
    path("dang-ky/", views.dangky, name='dangky'),
    path("dang-nhap/", auth_views.LoginView.as_view(template_name='simso/page-user/dangnhap.html',
                                                    extra_context={
                                                        "stl": SimTheoLoai.objects.all(),
                                                        "sns": SimNamSinh.objects.all(),
                                                        "nm": NhaMang.objects.all(),
                                                        # "stg": sorted(SimTheoGia.objects.all(), key=operator.attrgetter('title')),
                                                        "dmtt1": DanhMucTinTuc.objects.filter(TieuDe='Bạn cần biết'),
                                                        "bcbs": DanhMucTinTuc.objects.filter(TieuDe='Bạn cần biết').order_by('-NgayTao')[0:5],
                                                        "dmtt2": DanhMucTinTuc.objects.filter(TieuDe='Tin mới cập nhật'),
                                                        "tmcns": DanhMucTinTuc.objects.filter(TieuDe='Tin mới cập nhật').order_by('-NgayTao')[0:5],
                                                    }),
         name='dangnhap'),
    path("dang-xuat/", auth_views.LogoutView.as_view(next_page='/'), name='dangxuat'),
    path("thong-tin-tai-khoan/", views.thongtintaikhoan, name='thongtintaikhoan'),
    path("doi-mat-khau/", views.doimatkhau, name='doimatkhau'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    path("xac-thuc/", views.verify, name='xacthuc'),
    path("xac-thuc-sdt/", views.checkcode, name='xacthucsdt'),

]
