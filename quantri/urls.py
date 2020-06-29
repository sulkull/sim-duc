from django.urls import path, re_path

from quantri.views.daugia import *
from quantri.views.donhang import *
from quantri.views.loaisim import *
from quantri.views.main import *
from quantri.views.mang import *
from quantri.views.sanpham import *
from quantri.views.cauhinh import *
from quantri.views.tintuc import *

app_name = 'quantri'

urlpatterns = [
    path('', main, name='main'),
    path('error', Quyen404, name='Quyen-truy-cap'),

    # san pham
    path('sanpham/them',ThemSanPham.as_view(),name='Them-san-pham'),
    path('sanpham/sua/<id>',SuaSanPham,name='Sua-san-pham'),
    path('sanpham/danh-sach',DanhSachSanPham.as_view(),name='Danh-sach-san-pham'),
    path('sanpham/xoa/<id>',XoaSanPham.as_view(),name='xoa-san-pham'),

    # nha mang
    path('mang/them/',ThemMang.as_view(),name='Them-mang'),
    path('mang/them/<id>',Suamang,name='Sua-mang'),
    path('mang/xoa/<id>',XoaMang.as_view(),name='xoa-mang'),

    # loai sim
    path('loai/them/',ThemLoaiSim.as_view(),name='Them-loai'),
    path('loai/them/<id>',Sualoaisim,name='Sua-loai'),
    path('loai/xoa/<id>',Xoaloaisim.as_view(),name='xoa-loai'),

    #cau hinh
    path('cau-hinh/cau-hinh-trang/',SuaCauHinhTrang,name='cau-hinh-trang'),
    path('cau-hinh/cau-hinh-seo/',SuaCauHinhSEO,name='cau-hinh-seo'),

    #tin tuc
    path('tin-tuc/danh-muc/',DanhSachLoaiTinTuc.as_view(),name='danh-sach-loai-tin-tuc'),
    path('tin-tuc/danh-muc/them-moi/',ThemLoaiTinTuc.as_view(),name='them-loai-tin-tuc'),
    path('tin-tuc/danh-muc/sua/<id>',SuaLoaiTinTuc,name='sua-loai-tin-tuc'),
    path('tin-tuc/danh-muc/xoa/<id>',XoaDanhMucTinTuc.as_view(),name='xoa-loai-tin-tuc'),

    path('tin-tuc/danh-sach-tin-tuc/',DanhSachTinTuc.as_view(),name='danh-sach-tin-tuc'),
    path('tin-tuc/danh-sach-tin-tuc/them-moi/',ThemTinTuc.as_view(),name='them-tin-tuc'),
    path('tin-tuc/danh-sach-tin-tuc/sua/<id>',SuaTinTuc,name='sua-tin-tuc'),
    path('tin-tuc/danh-sach-tin-tuc/xoa/<id>',XoaTinTuc.as_view(),name='xoa-tin-tuc'),

    #don hang
    path('donhang',DanhSachDonHang.as_view(),name='danh-sach-don-hang'),
    path('donhang/<id>',UpdateDonHang,name='cap-nhat-don-hang'),
    path('donhang/xoa/<id>',XoaDonHang.as_view(),name='xoa-don-hang'),

    # dau gia
    path('daugia',DanhSachDauGia.as_view(),name='danh-sach-dau-gia'),
    path('daugia/them/',Themdaugia.as_view(),name='them-dau-gia'),
    path('daugia/sua/<id>',Suadaugia,name='sua-dau-gia'),
    path('daugia/xoa/<id>',Xoadaugia.as_view(),name='xoa-dau-gia'),
]
