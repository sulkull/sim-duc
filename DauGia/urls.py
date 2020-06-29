from django.urls import path
from . import views

app_name = 'DauGia'
urlpatterns = [
    path('', views.home, name='DauGia'),
    path('chi-tiet-dau-gia/<str:DuongDan>', views.chitietdaugia, name='chitietdaugia'),
    path('mua-luon/<str:DuongDan>', views.mualuon, name='mualuon'),
]