import django_filters
from django import forms
from sanpham.models import SanPham, NhaMang, SimTheoLoai, SimNamSinh


class SimFilter(django_filters.FilterSet):

    Mang = django_filters.ModelChoiceFilter(queryset=NhaMang.objects.all(),
                                                      widget=forms.Select)
    LoaiSims = django_filters.ModelChoiceFilter(queryset=SimTheoLoai.objects.all(),
                                            widget=forms.Select)
    NamSinh = django_filters.ModelChoiceFilter(queryset=SimNamSinh.objects.all(),
                                                widget=forms.Select)

    class Meta:
        model = SanPham
        fields = ['SoSim', 'Mang', 'LoaiSims','Gia','NamSinh','LoaiGia']