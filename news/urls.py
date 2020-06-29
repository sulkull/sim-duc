from django.urls import path
from . import views

app_name = 'tintuc'
urlpatterns = [
    path('', views.home, name='news'),
    path("danh-muc/<str:DuongDan>/", views.danhmuctintuc, name='danhmuctintuc'),
    path("<str:DuongDan>/", views.tintuc, name='tintuc'),
]
