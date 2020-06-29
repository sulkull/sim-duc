from django import forms
import re
from .models import CustomerUser
from django.core.exceptions import ObjectDoesNotExist


class DangKyForm(forms.Form):

    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tài khoản','label':'Tài khoản'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mật khẩu'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Nhập lại mật khẩu'}))
    firstname = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Họ'}))
    lastname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tên'}))
    choices = [('0', 'Nam'), ('1', 'Nữ'), ('2', 'Không xác định')]
    gioitinh = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'ul-none'}))
    ngaysinh = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Ngày sinh', 'type': 'date'}))
    sdt = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Số điện thoại'}))
    diachi = forms.CharField(max_length=400, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Địa chỉ'}))

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
            raise forms.ValidationError("Mật khẩu không đúng")

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Tên tài khoản có chứa ký tự đặc biệt")
        try:
            CustomerUser.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Tài khoản đã tồn tại")

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            CustomerUser.objects.get(email=email)
        except ObjectDoesNotExist:
            return email
        raise forms.ValidationError("Email đã tồn tại")

    def clean_sdt(self):
        sdt = self.cleaned_data['sdt']
        try:
            CustomerUser.objects.get(SDT=sdt)
        except ObjectDoesNotExist:
            return sdt
        raise forms.ValidationError("Số điện thoại đã tồn tại")

    def save(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password2']
        email = self.cleaned_data['email']
        firstname = self.cleaned_data['firstname']
        lastname = self.cleaned_data['lastname']
        gioitinh = self.cleaned_data['gioitinh']
        ngaysinh = self.cleaned_data['ngaysinh']
        sdt = self.cleaned_data['sdt']
        diachi = self.cleaned_data['diachi']

        CustomerUser.objects.create_user(username=username,
                                         password=password,
                                         email=email,
                                         first_name=firstname,
                                         last_name=lastname,
                                         GioiTinh=gioitinh,
                                         NgaySinh=ngaysinh,
                                         SDT=sdt,
                                         DiaChi=diachi,
                                         is_active=False)

    def getiduser(self):
        return CustomerUser.objects.get(username=self.cleaned_data['username'])

class ThongTinForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    firstname = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    lastname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    choices = [('0', 'Nam'), ('1', 'Nữ'), ('2', 'Không xác định')]
    gioitinh = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'form-check-input ul-none'}))
    ngaysinh = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    sdt = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    diachi = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ThongTinForm, self).__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data['email']
        if not CustomerUser.objects.filter(email=email).exclude(id=self.user.id):
            return email
        raise forms.ValidationError("Email đã tồn tại")

    def clean_sdt(self):
        sdt = self.cleaned_data['sdt']
        if not CustomerUser.objects.filter(SDT=sdt).exclude(id=self.user.id):
            return sdt
        raise forms.ValidationError("Số điện thoại đã tồn tại")


class DoiMatKhauForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mật khẩu'}))
    newpassword = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mật khẩu mới'}))
    renewpassword = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Nhập lại mật khẩu mới'}))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(DoiMatKhauForm, self).__init__(*args, **kwargs)

    def clean_password(self):
        password = self.cleaned_data['password']
        if self.user.check_password(password):
            print(password)
            print(self.user.password)
            return password
        raise forms.ValidationError("Mật khẩu không đúng")

    def clean_renewpassword(self):
        if 'newpassword' in self.cleaned_data:
            newpassword = self.cleaned_data['newpassword']
            renewpassword = self.cleaned_data['renewpassword']
            if newpassword == renewpassword and newpassword:
                return renewpassword
            raise forms.ValidationError("Mật khẩu mới không đúng")