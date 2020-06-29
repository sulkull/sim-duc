from django import forms
from sanpham.models import NhaMang, SimTheoGia


class JobFilterForm(forms.Form):
	NhaMang__id = forms.ModelChoiceField(queryset=NhaMang.objects.all(),widget=forms.Select(attrs={"class":"form-control","style":"width:220px"}))
	SimTheoGia__id = forms.ModelChoiceField(queryset=SimTheoGia.objects.all(),widget=forms.Select(attrs={"class":"form-control","style":"width:220px"}))
