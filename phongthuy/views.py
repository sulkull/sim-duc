from django.db.models import Q
from django.shortcuts import render
from phongthuy.models import Datapt, namsinh, nguhanh
from sanpham.models import SanPham, SimTheoLoai, SimNamSinh, NhaMang, SimTheoGia
from hoadon.models import HoaDon

import operator

def diem(request):
    data = Datapt.objects.all()
    data_ns = namsinh.objects.all()
    data_nh = nguhanh.objects.all()

    ngay = request.GET.get('ngay')
    if ngay:
        data = data.filter(
            Q(ngay=ngay)

        )
    thang = request.GET.get('thang')
    if thang:
        data = data.filter(
            Q(thang=thang)

        )
    nam = request.GET.get('namsinh')
    if nam:
        data = data_ns.filter(
            Q(namsinh__icontains=nam)

        )
    menh = request.GET.get('menh')
    if menh:
        data = data_nh.filter(
            Q(name__icontains=menh)

        )
    sp = SanPham.objects.filter(DaBan=False)
    simnamsinh = request.GET.get('namsinh')
    if simnamsinh:
        sp = sp.filter(
            Q(SoSim__icontains=ngay) and Q(SoSim__icontains=thang) or Q(SoSim__icontains=nam)
        )[0:50]
    
    stl = SimTheoLoai.objects.all()
    sns = SimNamSinh.objects.all()
    nm = NhaMang.objects.all()
    stg = SimTheoGia.objects.all()
    hd = HoaDon.objects.order_by('-NgayDatHang')[0:5]

    # Sắp xếp danh mục sim theo giá theo title
    stg_dsx = sorted(stg, key=operator.attrgetter('title'))

    pt = {
        'hd': hd,
        'stl': stl,
        'sns': sns,
        'nm': nm,
        'stg': stg_dsx,
        'data':data,
        'sp':sp,
        'data_ns':data_ns,
        'ngay':ngay,
        'thang':thang,
        'nam':nam,
        'menh':menh,
    }
    return render(request, 'simso/sub/kiem.html',pt)


