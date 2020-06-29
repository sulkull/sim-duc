from django.urls import path
from . import views

app_name = 'giohang'
urlpatterns = [
    path('', views.cart_home, name='home'),
    path('cap-nhat/', views.cart_update, name='update'),
    path('xoa/', views.cart_delete, name='delete'),
    path('xoa-tat-ca/', views.cart_deleteall, name='deleteall'),
    #path('updatesl/', views.cart_updatesl, name='updatesl'),
    path('gio-hang-trong/', views.cart_empty, name='giohangtrong'),
    path('thanh-toan/', views.checkout_home, name='checkout'),
    path('thanh-cong/', views.thanhcong, name='thanhcong'),
]