from gettext import gettext
from django import forms

from news.models import TinTuc, DanhMucTinTuc


class ThemTinTucForm(forms.ModelForm):
    class Meta:
        model = TinTuc
        fields = '__all__'
        exclude = ['DuongDan']
        widgets = {
            'LoaiTinTuc': forms.Select(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Chọn loại tin tức',
                'required': False
            },choices=DanhMucTinTuc.objects.all()),
            'TieuDe': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Nhập tiêu đề',
                'required': False
            }),
            'MoTaNgan': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Nhập mô tả ngắn',
                'required': False
            }),
            'NoiDung': forms.Textarea(attrs={
                'class': 'summernote',
                'placeholder': 'Nhập nội dung',
                'required': False
            }),
        }


class ThemLoaiTinTucForm(forms.ModelForm):
    class Meta:
        model = DanhMucTinTuc
        fields = '__all__'
        exclude = ['DuongDan']
        widgets = {
            'TieuDe': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Nhập tiêu đề',
                'required': False
            }),
        }

