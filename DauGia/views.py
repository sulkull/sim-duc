from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse

from sanpham.models import SimNamSinh, SimTheoGia, SimTheoLoai, NhaMang
from hoadon.models import HoaDon
import operator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import date
from .models import DauGia
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from user.models import CustomerUser

# Create your views here.
def home(request):
    # Lấy dữ liệu từ database
    daugia = DauGia.objects.filter(NgayHetHan__gte=date.today())#.order_by('-NgayHetHan')
    stl = SimTheoLoai.objects.all()
    sns = SimNamSinh.objects.all()
    nm = NhaMang.objects.all()
    stg = SimTheoGia.objects.all()
    hd = HoaDon.objects.order_by('-NgayDatHang')[0:5]

    stg_dsx = sorted(stg, key=operator.attrgetter('title'))
    
    # Phân trang
    page = request.GET.get('page', 1)
    paginator = Paginator(daugia, 12)
    try:
        DauGias = paginator.page(page)
    except PageNotAnInteger:
        DauGias = paginator.page(1)
    except EmptyPage:
        DauGias = paginator.page(paginator.num_pages)

    Data = {
            "daugia": DauGias,
            "stl": stl,
            "sns": sns,
            "nm": nm,
            "stg": stg_dsx,
            "hd": hd,
            }
    return render(request, 'simso/page-daugia/list-daugia.html', Data)

def chitietdaugia(request, DuongDan):
    if request.user.is_authenticated == False:
        return redirect('/user/dang-nhap/')
    # Lấy dữ liệu từ database
    try:
        daugia = DauGia.objects.get(DuongDan=DuongDan, NgayHetHan__gte=date.today())
    except DauGia.DoesNotExist:
        return redirect('DauGia:DauGia')

    stl = SimTheoLoai.objects.all()
    sns = SimNamSinh.objects.all()
    nm = NhaMang.objects.all()
    stg = SimTheoGia.objects.all()
    hd = HoaDon.objects.order_by('-NgayDatHang')[0:5]
    message = ""

    if request.method == 'POST':
        daugia = DauGia.objects.filter(DuongDan=request.POST.get('DuongDan'))[0]
        if (float)(request.POST.get('GiaDauGia')) >= (daugia.GiaHienTai + daugia.GiaToiThieu):
            daugia.GiaHienTai = request.POST.get('GiaDauGia')
            daugia.NguoiDauGiaHienTai = request.user
            daugia.save()
            return redirect('DauGia:chitietdaugia', daugia.DuongDan)
        else:
            message = "Giá đấu giá không hợp lệ"

    Data = {'daugia': daugia,
            "hd": hd,
            "stl": stl,
            "sns": sns,
            "nm": nm,
            "msg": message,
            }
    return render(request, 'simso/page-daugia/detail-daugia.html', Data)

def mualuon(request, DuongDan):
    if request.method == 'POST':
        daugia = DauGia.objects.filter(DuongDan=request.POST.get('DuongDan'))[0]
        daugia.GiaHienTai = daugia.GiaMuaLuon
        daugia.NguoiDauGiaHienTai = request.user
        daugia.DaDauGia = True
        daugia.save()

        #Gửi thông tin hóa đơn cho người dùng và admin
        user = request.user
        import pdb; pdb.set_trace()
        mail_subject = '[Sim Đức Lộc] Thông tin đấu giá.'
        message = render_to_string('simso/page-daugia/thongtindaugia.html', {
            'user': user,
            'DauGia': daugia,
        })
        to_email = user.email
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.content_subtype = 'html'
        email.mixed_subtype = 'related'
        email.send()


        mail_subject_admin = 'Đấu giá kết thúc.'
        message_admin = render_to_string('simso/page-daugia/thongtindaugiaadmin.html', {
            'User': user,
            'DauGia': daugia,
        })
        to_email_admins = CustomerUser.objects.get(is_superuser=True).email
        email_admin = EmailMessage(
            mail_subject_admin, message_admin, to=[to_email_admins]
        )
        email_admin.content_subtype = 'html'
        email_admin.mixed_subtype = 'related'
        email_admin.send()

        return redirect('DauGia:chitietdaugia', daugia.DuongDan)
