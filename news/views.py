from django.shortcuts import render
from .models import TinTuc, DanhMucTinTuc
from sanpham.models import SimTheoGia, SimNamSinh, SimTheoLoai, NhaMang
from hoadon.models import HoaDon
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import operator

# Create your views here.
def home(request):
    # Lấy dữ liệu từ database
    tintuc = TinTuc.objects.all().order_by('-NgayTao')
    dmtt1 = DanhMucTinTuc.objects.get(TieuDe='Bạn cần biết')
    bcbs = dmtt1.tintuc_set.order_by('-NgayTao')[0:5]
    dmtt2 = DanhMucTinTuc.objects.get(TieuDe='Tin mới cập nhật')
    tmcns = dmtt2.tintuc_set.order_by('-NgayTao')[0:5]
    stl = SimTheoLoai.objects.all()
    sns = SimNamSinh.objects.all()
    nm = NhaMang.objects.all()
    stg = SimTheoGia.objects.all()
    hd = HoaDon.objects.order_by('-NgayDatHang')[0:5]

    stg_dsx = sorted(stg, key=operator.attrgetter('title'))
    
    # Phân trang
    page = request.GET.get('page', 1)
    paginator = Paginator(tintuc, 6)
    try:
        TinTucs = paginator.page(page)
    except PageNotAnInteger:
        TinTucs = paginator.page(1)
    except EmptyPage:
        TinTucs = paginator.page(paginator.num_pages)

    Data = {"TinTucs": TinTucs,
            "dmtt1": dmtt1,
            "bcbs": bcbs,
            "dmtt2": dmtt2,
            "tmcns": tmcns,
            "stl": stl,
            "sns": sns,
            "nm": nm,
            "stg": stg_dsx,
            "hd": hd,
            }
    return render(request, 'simso/news/news.html', Data)

def danhmuctintuc(request, DuongDan):
    DanhMuc_obj = DanhMucTinTuc.objects.get(DuongDan=DuongDan)
    TinTucs_obj = DanhMuc_obj.tintuc_set.all()
    dmtt1 = DanhMucTinTuc.objects.get(TieuDe='Bạn cần biết')
    bcbs = dmtt1.tintuc_set.order_by('-NgayTao')[0:5]
    dmtt2 = DanhMucTinTuc.objects.get(TieuDe='Tin mới cập nhật')
    tmcns = dmtt2.tintuc_set.order_by('-NgayTao')[0:5]
    stl = SimTheoLoai.objects.all()
    sns = SimNamSinh.objects.all()
    nm = NhaMang.objects.all()
    stg = SimTheoGia.objects.all()
    hd = HoaDon.objects.order_by('-NgayDatHang')[0:5]
    stg_dsx = sorted(stg, key=operator.attrgetter('title'))

    # Phân trang
    page = request.GET.get('page', 1)
    paginator = Paginator(TinTucs_obj, 6)
    try:
        TinTucs = paginator.page(page)
    except PageNotAnInteger:
        TinTucs = paginator.page(1)
    except EmptyPage:
        TinTucs = paginator.page(paginator.num_pages)

    Data = {
            "TieuDe": DanhMuc_obj.TieuDe,
            "TinTucs": TinTucs,
            "dmtt1": dmtt1,
            "bcbs": bcbs,
            "dmtt2": dmtt2,
            "tmcns": tmcns,
            "stl": stl,
            "sns": sns,
            "nm": nm,
            "stg": stg_dsx,
            "hd": hd,
            }
    return render(request, 'simso/news/danh-muc-tin-tuc.html', Data)

def tintuc(request, DuongDan):
    # Lấy dữ liệu từ database
    tintuc = TinTuc.objects.get(DuongDan=DuongDan)
    stl = SimTheoLoai.objects.all()
    sns = SimNamSinh.objects.all()
    nm = NhaMang.objects.all()
    stg = SimTheoGia.objects.all()
    hd = HoaDon.objects.order_by('-NgayDatHang')[0:5]
    stg_dsx = sorted(stg, key=operator.attrgetter('title'))

    Data = {'TinTuc': tintuc,
            "TinTucKhacs": TinTuc.objects.all().order_by('-NgayTao').exclude(DuongDan=DuongDan)[:10],
            "stl": stl,
            "sns": sns,
            "nm": nm,
            "stg": stg_dsx,
            "hd": hd,
            }
    return render(request, 'simso/news/tin-tuc.html', Data)










