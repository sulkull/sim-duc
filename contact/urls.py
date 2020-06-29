from django.urls import path
from . import views

app_name = 'lienhe'
urlpatterns = [
    path('', views.home, name='contact'),
]