from django.contrib.auth.decorators import login_required
from django.db.models.aggregates import Sum
from django.shortcuts import render, redirect

# Create your views here.
from hoadon.models import HoaDon
from sanpham.models import SanPham
from user.models import CustomerUser



@login_required(login_url='/user/dang-nhap')
def main(request):
   if request.user.is_superuser:
      user = CustomerUser.objects.all()
      sim = SanPham.objects.all()
      hoadon = HoaDon.objects.all()
      tongtien = HoaDon.objects.filter(ThanhToan=True).aggregate(Sum('TongTien'))['TongTien__sum']
      # import pdb;pdb.set_trace()
   else:
      return redirect('sanpham:home')

   data = {
      'user':user,
      'sim':sim,
      'hoadon':hoadon,
      'tongtien':tongtien,
   }

   return render(request ,'quanly/page/dashboards.html',data)