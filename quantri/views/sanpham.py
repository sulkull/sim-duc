from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DeleteView

from quantri.froms.sanpham import ThemSanPhamForm
from sanpham.models import SanPham


@login_required(login_url='/user/dang-nhap')
def Quyen404(request):
    data = {"item": {'title': 'Lỗi truy cập'}}
    return render(request, 'quanly/page/404-user.html', data)


class ThemSanPham(SuccessMessageMixin,CreateView):
    model = SanPham
    form_class = ThemSanPhamForm
    template_name = 'quanly/page/them-san-pham.html'
    success_url = reverse_lazy('quantri:Them-san-pham')
    success_message = "Thêm sim thành công!"
    extra_context = {
        'class_tp': 'active',
        'item': 'Thêm sản phẩm mới'
    }
# Kiem tra quyen truy cap - Bao nhi
    @method_decorator(login_required(login_url=reverse_lazy('user:dangnhap')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('user:dangnhap')
        if self.request.user.is_authenticated and not self.request.user.is_superuser:
            return redirect('quantri:Quyen-truy-cap')
        return super().dispatch(self.request, *args, **kwargs)


@login_required
def SuaSanPham(request, id):
    obj = get_object_or_404(SanPham, id=id)
    form = ThemSanPhamForm(request.POST or None, instance=obj)
    context = {'form': form}

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "Cập nhật thông tin sim thành công")
        context = {'form': form}
        return render(request, 'quanly/page/them-san-pham.html', context)

    else:
        context = {'form': form,
                   'error': 'Có gì đó sai sai'}
        return render(request, 'quanly/page/them-san-pham.html', context)

class DanhSachSanPham(ListView):
    model = SanPham
    paginate_by = 200  # if pagination is desired
    template_name = 'quanly/page/danh-sach-san-pham.html'
    queryset = SanPham.objects.filter(DaBan=False)
    context_object_name = 'sanpham'
    extra_context = {
        'title': 'Danh sách sim',
        'item' : 'Danh sách sim'
    }
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['sp_daban'] = SanPham.objects.filter(DaBan=True)
        return data

class XoaSanPham(SuccessMessageMixin,DeleteView):
    template_name = 'quanly/page/xoa-post.html'
    success_message = "Xoá thành công!"
    success_url = reverse_lazy('quantri:Danh-sach-san-pham')
    extra_context = {
        'title': 'Xoá sim',
        'item': 'Xoá sim'
    }

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(SanPham, id=id_)