from django.urls import path
from timkiem import views

app_name='timkiem'
urlpatterns = [
     path('ajax/', views.timkiem_nangcao, name='timkiem_ajax'),
     path('', views.timkiem, name='timkiem'),


]
