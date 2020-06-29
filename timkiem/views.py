from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q
from django.template.loader import render_to_string

from sanpham.models import SimTheoGia ,NhaMang, SimTheoLoai , SimNamSinh ,SanPham

def timkiem_nangcao(request):
    sp = SanPham.objects.filter(DaBan=False)
    nm = NhaMang.objects.all()
    ns = SimNamSinh.objects.all()
    stl = SimTheoLoai.objects.all()
    stg = SimTheoGia.objects.all()
# tim theo nha mang
    nhamang = request.GET.get('nhamang')
    if nhamang:
        sp = sp.filter(
            Q(Mang__title__icontains=nhamang)

        )
# tim kiem theo nam sinh
    namsinh = request.GET.get('namsinh')
    if namsinh:
        sp = sp.filter(
            Q(NamSinh__title__icontains=namsinh)

        )
# tim kiem theo loai sim
    loai = request.GET.get('loai')
    if loai:
        sp = sp.filter(
            Q(LoaiSims__title__icontains=loai)

        )
# tim kiem theo muc gia
    mucgia = request.GET.get('mucgia')
    if mucgia:
        sp = sp.filter(
            Q(LoaiGia__title__icontains=mucgia)

        )
# tim theo so simmmm
    sosim = request.GET.get('so')
    if sosim :
        if '*' in sosim:
            sosim = sosim.split('*')
            if sosim[0] != '':
                sp = sp.filter(Q(SoSim__startswith=sosim[0]))
            if sosim[1] != '':
                sp = sp.filter(Q(SoSim__endswith=sosim[1]))
        else:
            if sosim:
                sp = sp.filter(Q(SoSim__icontains=sosim))

    context = {
        "sanpham": sp,
        "ns": ns,
        "nhamang": nhamang,
        "loai": loai,
        "mucgia": mucgia,
        "stl": stl,
        "stg": stg,
        "nm": nm,
    }
    data = dict()
    data['html'] = render_to_string('includes/timkiem/showtimkiem.html', context, request=request)
    return JsonResponse(data,status=200)
    # return render(request, 'includes/timkiem/ketqua-timkiem.html', context)

def timkiem(request):
    sp = SanPham.objects.filter(DaBan=False)
# tim theo so simmmm
    sosim = request.GET.get('so')
    if sosim :
        if '*' in sosim:
            sosim = sosim.split('*')
            if sosim[0] != '':
                sp = sp.filter(Q(SoSim__startswith=sosim[0]))
            if sosim[1] != '':
                sp = sp.filter(Q(SoSim__endswith=sosim[1]))
        else:
            if sosim:
                sp = sp.filter(Q(SoSim__icontains=sosim))

    context = {
        "sp": sp,
    }
    return render(request, 'includes/timkiem/ketqua-timkiem.html', context)
