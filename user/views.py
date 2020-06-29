import operator

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView

from sanpham.models import *
from .forms import DangKyForm, ThongTinForm, DoiMatKhauForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from user.models import CustomerUser
from django.contrib.auth import login, authenticate
from hoadon.models import HoaDon
from news.models import TinTuc, DanhMucTinTuc

import nexmo


class Dataview(ListView):
    model = SanPham
    context_object_name = 'sp'
    queryset = SanPham.objects.filter(DaBan=False)

    def get_context_data(self, **kwargs):
        context = super(Dataview, self).get_context_data(**kwargs)
        context['stl'] = SimTheoLoai.objects.all()
        context['sns'] = SimNamSinh.objects.all()
        context['nm'] = NhaMang.objects.all()
        context['stg'] = SimTheoGia.objects.all()
        context['hd'] = HoaDon.objects.order_by('-NgayDatHang')[0:9]

        # Sắp xếp danh mục sim theo giá theo title
        return context


# Create your views here.
def dangky(request):
    #########
    stl = SimTheoLoai.objects.all()
    sns = SimNamSinh.objects.all()
    nm = NhaMang.objects.all()
    stg = SimTheoGia.objects.all()
    hd = HoaDon.objects.order_by('-NgayDatHang')[0:5]

    # Sắp xếp danh mục sim theo giá theo title
    stg_dsx = sorted(stg, key=operator.attrgetter('title'))
    ########
    form = DangKyForm()
    if request.method == 'POST':
        form = DangKyForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['user_id'] = form.getiduser().id
            return redirect('user:xacthuc')

    Data = {
        'form': form,
        "hd": hd,
        "stl": stl,
        "sns": sns,
        "nm": nm,
        "stg": stg_dsx,

    }

    return render(request, 'simso/page-user/dangky.html', Data)


def verify(request):
    id = request.session['user_id']
    user = CustomerUser.objects.get(id=id)

    stl = SimTheoLoai.objects.all()
    sns = SimNamSinh.objects.all()
    nm = NhaMang.objects.all()
    stg = SimTheoGia.objects.all()
    hd = HoaDon.objects.order_by('-NgayDatHang')[0:5]


    # Sắp xếp danh mục sim theo giá theo title
    stg_dsx = sorted(stg, key=operator.attrgetter('title'))

    Data = {
        "hd": hd,
        "stl": stl,
        "sns": sns,
        "nm": nm,
        "stg": stg_dsx,

    }

    if request.method == 'POST':
        if request.POST.get("verify") == 'sdt':
            key = 'd3541bdb'
            secret = '9Tn3HaqVhJX1pVKW'
            sdt = "+84{}".format(user.SDT)
            client = nexmo.Client(key=key, secret=secret)

            response = client.start_verification(
                number=sdt,
                brand="SimSoDucLoc",
                code_length="4")
            request.session['request_id'] = response["request_id"]
            return redirect('user:xacthucsdt')
        else:
            current_site = get_current_site(request)
            mail_subject = 'Kích hoạt tài khoản của bạn.'
            message = render_to_string('simso/page-user/activeemail.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = user.email
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return render(request, 'simso/page-user/success.html', Data)

    return render(request, 'simso/page-user/verify.html', Data)


def checkcode(request):
    error = ""
    key = 'd3541bdb'
    secret = '9Tn3HaqVhJX1pVKW'
    client = nexmo.Client(key=key, secret=secret)
    request_id = request.session['request_id']

    stl = SimTheoLoai.objects.all()
    sns = SimNamSinh.objects.all()
    nm = NhaMang.objects.all()
    stg = SimTheoGia.objects.all()
    hd = HoaDon.objects.order_by('-NgayDatHang')[0:5]


    Data = {
        "hd": hd,
        "stl": stl,
        "sns": sns,
        "nm": nm,
        "stg": stg,

    }

    if request.method == 'POST':
        code = request.POST.get('code')
        response = client.check_verification(request_id, code=code)
        if response["status"] == "0":
            id = request.session['user_id']
            user = CustomerUser.objects.get(id=id)
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('sanpham:home')
        else:
            error = "Mã xác thực không đúng!!!"
    return render(request, 'simso/page-user/confirm.html', Data)

def activate(request, uidb64, token):
    stl = SimTheoLoai.objects.all()
    sns = SimNamSinh.objects.all()
    nm = NhaMang.objects.all()
    stg = SimTheoGia.objects.all()
    hd = HoaDon.objects.order_by('-NgayDatHang')[0:5]


    Data = {
        "hd": hd,
        "stl": stl,
        "sns": sns,
        "nm": nm,
        "stg": stg,

    }

    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = CustomerUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, CustomerUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('sanpham:home')
    else:
        return render(request, 'simso/page-user/error.html', Data)


def thongtintaikhoan(request):
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect('/user/dang-nhap/')

    stl = SimTheoLoai.objects.all()
    sns = SimNamSinh.objects.all()
    nm = NhaMang.objects.all()
    stg = SimTheoGia.objects.all()
    hd = HoaDon.objects.order_by('-NgayDatHang')[0:5]

    # Sắp xếp danh mục sim theo giá theo title

    firstname = user.first_name
    lastname = user.last_name
    email = user.email
    sdt = user.SDT
    diachi = user.DiaChi
    gioitinh = user.GioiTinh
    ngaysinh = user.NgaySinh

    data = {'firstname': firstname,
            'lastname': lastname,
            'email': email,
            'sdt': sdt,
            'diachi': diachi,
            'gioitinh': gioitinh,
            'ngaysinh': ngaysinh}

    form = ThongTinForm(initial=data)

    if request.method == 'POST':
        form = ThongTinForm(request.POST, user=request.user)
        #Kiểm tra thông tin
        if form.is_valid():
            if form['email'].value() is not None:
                email = form['email'].value()
            if form['sdt'].value() is not None:
                sdt = form['sdt'].value()
            if form['firstname'].value() is not None:
                firstname = form['firstname'].value()
            if form['lastname'].value() is not None:
                lastname = form['lastname'].value()
            if form['diachi'].value() is not None:
                diachi = form['diachi'].value()
            if form['gioitinh'].value() is not None:
                gioitinh = form['gioitinh'].value()
            if form['ngaysinh'].value() is not None:
                ngaysinh = form['ngaysinh'].value()

        user.email = email
        user.SDT = sdt
        user.first_name = firstname
        user.last_name = lastname
        user.DiaChi = diachi
        user.GioiTinh = gioitinh
        user.NgaySinh = ngaysinh
        user.save()
    Data = {"User": user,
            "form": form,
            "hd": hd,
            "stl": stl,
            "sns": sns,
            "nm": nm,
            "stg": stg,

            }
    return render(request, 'simso/page-user/thongtintaikhoan.html', Data)


def doimatkhau(request):
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect('/user/dang-nhap/')
    form = DoiMatKhauForm()

    stl = SimTheoLoai.objects.all()
    sns = SimNamSinh.objects.all()
    nm = NhaMang.objects.all()
    stg = SimTheoGia.objects.all()
    hd = HoaDon.objects.order_by('-NgayDatHang')[0:5]

    if request.method == 'POST':
        form = DoiMatKhauForm(request.POST, user=request.user)
        #Kiểm tra thông tin
        if form.is_valid():
            user.set_password(form['renewpassword'].value())
            user.save()
            return HttpResponseRedirect('/user/dang-nhap/')

    Data = {"form": form,
            "hd": hd,
            "stl": stl,
            "sns": sns,
            "nm": nm,
            "stg": stg,

            }
    return render(request, 'simso/page-user/doimatkhau.html', Data)
