from gettext import gettext
from django import forms

from sanpham.models import SanPham, SIM_CHOICES


class ThemSanPhamForm(forms.ModelForm):
    class Meta:
        model = SanPham
        fields = '__all__'
        exclude = ['slug','luotxem','LoaiGia']
        # labels = {
        # }
        widgets = {
            'SoSim': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Nhập số sim',
                'required': False
            }),
            'DaBan': forms.CheckboxInput(attrs={
                'class': 'input input--switch border',
            }),
            'Gia': forms.NumberInput(attrs={
                'class': 'input pr-16 w-full border col-span-4',
                'placeholder': '500000',
                'required': False
            }),
            'Mang': forms.Select(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Chọn nhà mạng',
                'required': False
            }),
            'NamSinh': forms.Select(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Chọn năm sinh',
                'required': False
            }),
            'TacVu': forms.Select(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Nơi hiển thị ở trang chủ',
                'required': False
            },choices=SIM_CHOICES),
            'LoaiSims': forms.SelectMultiple(attrs={
                'class': 'select2 w-full',
                'multiple': True,
                'required': False
            }),
        }