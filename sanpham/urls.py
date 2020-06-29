from django.urls import path

from . import views

app_name = 'sanpham'
urlpatterns = [
    path('', views.index, name='home'),
    path("san-pham/<str:slug>", views.sanpham, name='sanpham'),
    path('sim-theo-gia/<str:slug>', views.simtheogia, name='simtheogia'),
    path('sim-theo-mang/<str:slug>', views.simtheomang, name='simtheomang'),
    path('sim-theo-loai/<str:slug>', views.simtheoloai, name='simtheoloai'),
    path('sim-nam-sinh/<str:slug>', views.simnamsinh, name='simnamsinh'),


]
