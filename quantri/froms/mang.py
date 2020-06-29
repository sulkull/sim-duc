from django import forms
from sanpham.models import NhaMang


class ThemNhaMangForm(forms.ModelForm):
    class Meta:
        model = NhaMang
        fields = '__all__'
        exclude = ['slug']
        # labels = {
        # }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Nhập tên nhà mạng',
                'required': False
            }),
        }