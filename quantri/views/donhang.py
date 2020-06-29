from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DeleteView

from hoadon.models import HoaDon
from quantri.froms.donhang import DonHangForm
from quantri.froms.sanpham import ThemSanPhamForm
from sanpham.models import SanPham


@login_required(login_url='/user/dang-nhap')
def Quyen404(request):
    data = {"item": {'title': 'Lỗi truy cập'}}
    return render(request, 'quanly/page/404-user.html', data)

@login_required
def UpdateDonHang(request, id):
    obj = get_object_or_404(HoaDon, id=id)
    hoadon = HoaDon.objects.get(id=id)
    form = DonHangForm(request.POST or None, instance=obj)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "Cập nhật thông tin sim thành công")
        context = {'form': form,
                   'hoadon':hoadon,}
        return render(request, 'quanly/page/don-hang.html', context)
    else:
        context = {'form': form,
                   'hoadon': hoadon,
                   'error': 'Có gì đó sai sai'}
        return render(request, 'quanly/page/don-hang.html', context)

class DanhSachDonHang(ListView):
    model = HoaDon
    paginate_by = 20  # if pagination is desired
    template_name = 'quanly/page/danh-sach-don-hang.html'
    queryset = HoaDon.objects.filter(GiaoHang=False)
    context_object_name = 'donhang'
    extra_context = {
        'title': 'Danh sách đơn hàng',
        'item' : 'Danh sách đơn hàng'
    }
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['dagiao'] = HoaDon.objects.filter(GiaoHang=True)
        return data

class XoaDonHang(SuccessMessageMixin,DeleteView):
    template_name = 'quanly/page/xoa-post.html'
    success_message = "Xoá thành công!"
    success_url = reverse_lazy('quantri:danh-sach-don-hang')
    extra_context = {
        'title': 'Xoá đơn hàng',
        'item': 'Xoá đơn hàng'
    }

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(HoaDon, id=id_)