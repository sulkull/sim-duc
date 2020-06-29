from django import forms
from hoadon.models import HoaDon


class DonHangForm(forms.ModelForm):
    class Meta:
        model = HoaDon
        fields = '__all__'
        exclude = ['GH','NgayDatHang','TongTien']
        # labels = {
        # }
        widgets = {
            'HoTenNguoiNhan': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Họ tên người nhận',
                'required': False
            }),
            'DiaChiNguoiNhan': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Địa chỉ',
                'required': False
            }),

            'SDT': forms.NumberInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Nhập số điện thoại',
                'required': False
            }),
            'ThanhToan': forms.CheckboxInput(attrs={
                'class': 'input input--switch border',
                'required': False
            }),
            'GiaoHang': forms.CheckboxInput(attrs={
                'class': 'input input--switch border',
                'required': False
            }),
        }