from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DeleteView

from quantri.froms.tintuc import ThemTinTucForm, ThemLoaiTinTucForm
from news.models import TinTuc, DanhMucTinTuc


@login_required(login_url='/user/dang-nhap')
def Quyen404(request):
    data = {"item": {'title': 'Lỗi truy cập'}}
    return render(request, 'quanly/page/404-user.html', data)


class ThemLoaiTinTuc(SuccessMessageMixin,CreateView):
    model = DanhMucTinTuc
    form_class = ThemLoaiTinTucForm
    template_name = 'quanly/page/tintuc/them-loai-tin-tuc.html'
    success_url = reverse_lazy('quantri:danh-sach-loai-tin-tuc')
    success_message = "Thêm loại tin tức thành công!"
    extra_context = {
        'class_tp': 'active',
        'title': 'Thêm loại tin tức mới',
        'item': 'Thêm loại tin tức mới'
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
def SuaLoaiTinTuc(request, id):
    obj = get_object_or_404(DanhMucTinTuc, id=id)
    form = ThemLoaiTinTucForm(request.POST or None, instance=obj)
    context = {'form': form,
                'title': 'Sửa loại tin tức',
                'item': 'Sửa loại tin tức'}

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "Cập nhật thông tin danh mục tin tức thành công")
        context = {'form': form,
                    'title': 'Sửa loại tin tức',
                    'item': 'Sửa loại tin tức'}
        return render(request, 'quanly/page/tintuc/them-loai-tin-tuc.html', context)

    else:
        context = {'form': form,
                    'title': 'Sửa loại tin tức',
                    'item': 'Sửa loại tin tức',
                   'error': 'Có gì đó sai sai'}
        return render(request, 'quanly/page/tintuc/them-loai-tin-tuc.html', context)

class ThemTinTuc(SuccessMessageMixin,CreateView):
    model = TinTuc
    form_class = ThemTinTucForm
    template_name = 'quanly/page/tintuc/them-tin-tuc.html'
    success_url = reverse_lazy('quantri:danh-sach-tin-tuc')
    success_message = "Thêm tin tức thành công!"
    extra_context = {
        'class_tp': 'active',
        'title': 'Thêm tin tức mới',
        'item': 'Thêm tin tức mới'
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
def SuaTinTuc(request, id):
    obj = get_object_or_404(TinTuc, id=id)
    form = ThemTinTucForm(request.POST or None, instance=obj)
    context = {'form': form,
                'title': 'Sửa tin tức',
                'item': 'Sửa tin tức'}

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "Cập nhật thông tin tin tức thành công")
        context = {'form': form,
                    'title': 'Sửa tin tức',
                    'item': 'Sửa tin tức'}
        return render(request, 'quanly/page/tintuc/them-tin-tuc.html', context)

    else:
        context = {'form': form,
                    'title': 'Sửa loại tin tức',
                    'item': 'Sửa loại tin tức',
                   'error': 'Có gì đó sai sai'}
        return render(request, 'quanly/page/tintuc/them-tin-tuc.html', context)

class DanhSachTinTuc(ListView):
    model = TinTuc
    paginate_by = 20  # if pagination is desired
    template_name = 'quanly/page/tintuc/tin-tuc.html'
    queryset = TinTuc.objects.all()
    context_object_name = 'tintuc'
    extra_context = {
        'title': 'Danh sách tin tức',
        'item' : 'Danh sách tin tức'
    }
   

class DanhSachLoaiTinTuc(ListView):
    model = DanhMucTinTuc
    paginate_by = 20  # if pagination is desired
    template_name = 'quanly/page/tintuc/danh-muc-tin-tuc.html'
    queryset = DanhMucTinTuc.objects.all()
    context_object_name = 'danhmuctintuc'
    extra_context = {
        'title': 'Danh sách loại tin tức',
        'item' : 'Danh sách loại tin tức'
    }
    

class XoaDanhMucTinTuc(SuccessMessageMixin,DeleteView):
    template_name = 'quanly/page/xoa-post.html'
    success_message = "Xoá thành công!"
    success_url = reverse_lazy('quantri:danh-sach-loai-tin-tuc')
    extra_context = {
        'title': 'Xoá danh mục',
        'item': 'Xoá  danh mục'
    }

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(DanhMucTinTuc, id=id_)

class XoaTinTuc(SuccessMessageMixin,DeleteView):
    template_name = 'quanly/page/xoa-post.html'
    success_message = "Xoá thành công!"
    success_url = reverse_lazy('quantri:danh-sach-tin-tuc')
    extra_context = {
        'title': 'Xoá tin',
        'item': 'Xoá tin'
    }

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(TinTuc, id=id_)