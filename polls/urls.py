from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('add/', views.add_car, name='add_car'),
    path(
        'car/<int:car_id>/', views.car_detail, name='car_detail'
    ),  # YENİ LİNK
]