from django.urls import path, re_path
from . import views

app_name = 'phongthuy'
urlpatterns = [
    re_path(r'xem-phong-thuy/$', views.diem, name='xem-phong-thuy'),
]