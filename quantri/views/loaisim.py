from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import model_to_dict
from django.http import JsonResponse, request
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, ListView, DeleteView

from quantri.froms.loaisim import ThemLoaiSimForm
from sanpham.models import SimTheoLoai


@login_required(login_url='/user/dang-nhap')
def Quyen404(request):
    data = {"item": {'title': 'Lỗi truy cập'}}
    return render(request, 'quanly/page/404-user.html', data)


class ThemLoaiSim(SuccessMessageMixin, CreateView):
    model = SimTheoLoai
    form_class = ThemLoaiSimForm
    template_name = 'quanly/page/loaisim/them.html'
    success_url = reverse_lazy('quantri:Them-loai')
    success_message = "Cập nhật thành công!"
    paginate_by = 5
    extra_context = {
        'class_tp': 'active',
        'item': 'Thêm nhà mạng'
    }
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['loaisim'] = SimTheoLoai.objects.order_by('-id')
        return data
    def post(self, request, *args, **kwargs):
        form = ThemLoaiSimForm(request.POST)
        if form.is_valid():
            new_data = form.save()
            return JsonResponse({'loaisim':model_to_dict(new_data)},status=200)
        else:
            return redirect('quantri:Them-loaisim')

    # Kiem tra quyen truy cap - duc
    @method_decorator(login_required(login_url=reverse_lazy('user:dangnhap')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('user:dangnhap')
        if self.request.user.is_authenticated and not self.request.user.is_superuser:
            return redirect('quantri:Quyen-truy-cap')
        return super().dispatch(self.request, *args, **kwargs)


@login_required
def Sualoaisim(request, id):
    loaisim = get_object_or_404(SimTheoLoai, id=id)
    data = dict()
    form = ThemLoaiSimForm(request.GET or None, instance=loaisim)
    if form.is_valid():
        form = form.save(commit=False)
        form.save()
        messages.success(request, "Cập nhật thông tin thành công")
        data['html'] = render_to_string('quanly/page/loaisim/sua.html', {'form': form}, request=request)
        data['html_kq'] = render_to_string('quanly/page/loaisim/list.html', {'form': form}, request=request)
    else:
        form = ThemLoaiSimForm(request.GET or None, instance=loaisim)
        data['html'] = render_to_string('quanly/page/loaisim/sua.html', {'form': form}, request=request)
        data['html_kq'] = render_to_string('quanly/page/loaisim/list.html', {'form': form}, request=request)
        return JsonResponse(data)

class Xoaloaisim(SuccessMessageMixin, DeleteView):
    template_name = 'quanly/page/xoa-post.html'
    success_message = "Xoá thành công phòng!"
    success_url = reverse_lazy('quantri:Them-loai')
    extra_context = {
        'title': 'Xoá sim',
        'item': 'Xoá sim'
    }
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(SimTheoLoai, id=id_)



