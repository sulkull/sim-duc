from django import forms
from sanpham.models import SimTheoLoai


class ThemLoaiSimForm(forms.ModelForm):
    class Meta:
        model = SimTheoLoai
        fields = '__all__'
        exclude = ['slug']
        # labels = {
        # }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Nhập loại sim',
                'required': False
            }),
        }