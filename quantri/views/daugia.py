from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DeleteView

from DauGia.models import DauGia
from quantri.froms.daugia import ThemDauGiaForm
from quantri.froms.sanpham import ThemSanPhamForm
from sanpham.models import SanPham


@login_required(login_url='/user/dang-nhap')
def Quyen404(request):
    data = {"item": {'title': 'Lỗi truy cập'}}
    return render(request, 'quanly/page/404-user.html', data)


class Themdaugia(SuccessMessageMixin,CreateView):
    model = DauGia
    form_class = ThemDauGiaForm
    template_name = 'quanly/page/daugia/them-dau-gia.html'
    success_url = reverse_lazy('quantri:danh-sach-dau-gia')
    success_message = "Thêm đấu giá thành công!"
    context_object_name = 'daugia'
    extra_context = {
        'class_tp': 'active',
        'title': 'Thêm đấu giá mới',
        'item': 'Thêm đấu giá mới'
    }
    
# Kiem tra quyen truy cap - duc
    @method_decorator(login_required(login_url=reverse_lazy('user:dangnhap')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('user:dangnhap')
        if self.request.user.is_authenticated and not self.request.user.is_superuser:
            return redirect('quantri:Quyen-truy-cap')
        return super().dispatch(self.request, *args, **kwargs)


@login_required
def Suadaugia(request, id):
    try:
        daugia = DauGia.objects.get(id=id)
    except DauGia.DoesNotExist:
        return redirect('quantri:danh-sach-dau-gia')
    form = ThemDauGiaForm(request.POST or None, instance=daugia)

    context = {'form': form}

    if form.is_valid():
        daugia = form.save(commit=False)
        daugia.save()
        messages.success(request, "Cập nhật thông tin đấu giá thành công")
        context = {'form': form,
                   'daugia':daugia,
                   'title': 'Thêm đấu giá mới',
                    'item': 'Thêm đấu giá mới'}
        return render(request, 'quanly/page/daugia/them-dau-gia.html', context)

    else:
        context = {'form': form,
                   'daugia':daugia,
                   'error': 'Có gì đó sai sai',
                   'title': 'Thêm đấu giá mới',
                    'item': 'Thêm đấu giá mới'}
        return render(request, 'quanly/page/daugia/them-dau-gia.html', context)

class DanhSachDauGia(ListView):
    model = DauGia
    # paginate_by = 20  # if pagination is desired
    template_name = 'quanly/page/daugia/danh-sach-dau-gia.html'
    queryset = DauGia.objects.filter(DaDauGia=False)
    context_object_name = 'daugia'
    extra_context = {
        'title': 'Danh sách sim đấu giá',
        'item' : 'Danh sách sim đấu giá'
    }
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['sp_dadaugia'] = DauGia.objects.filter(DaDauGia=True)
        return data

class Xoadaugia(SuccessMessageMixin,DeleteView):
    template_name = 'quanly/page/xoa-post.html'
    success_message = "Xoá thành công!"
    success_url = reverse_lazy('quantri:danh-sach-dau-gia')
    extra_context = {
        'title': 'Xoá đấu giá',
        'item': 'Xoá đấu giá'
    }

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(DauGia, id=id_)