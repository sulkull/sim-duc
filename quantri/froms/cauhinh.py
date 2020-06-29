from gettext import gettext
from django import forms

from CauHinh.models import CauHinhTrang, CauHinhSeo, Default_robot


class ThemCauHinhTrangForm(forms.ModelForm):
    class Meta:
        model = CauHinhTrang
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Nhập tiêu đề',
                'required': False
            }),
            'sdt1': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Nhập số điện thoại 1',
                'required': False
            }),
            'sdt2': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Nhập số điện thoại 2',
                'required': False
            }),
            'zalo': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Nhập mã zalo',
                'required': False
            }),
            'chatfb': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Nhập mã chat facebook',
                'required': False
            }),
            'footer': forms.Textarea(attrs={
                'class': 'summernote',
                'placeholder': 'Nhập footer',
                'required': False
            }),
        }

class ThemCauHinhSEOForm(forms.ModelForm):
    class Meta:
        model = CauHinhSeo
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Nhập tiêu đề',
                'required': False
            }),
            'keyword': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Nhập từ khóa',
                'required': False
            }),
            'des': forms.Textarea(attrs={
                'class': 'summernote',
                'placeholder': 'Nhập mô tả',
                'required': False
            }),
            'google': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Nhập mã google',
                'required': False
            }),
            'fb_app': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Nhập facebook app',
                'required': False
            }),
            'robots': forms.Select(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Nhập robots',
                'required': False
            },choices=Default_robot),
        }