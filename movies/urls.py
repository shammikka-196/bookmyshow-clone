from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('theaters/<int:movie_id>/', views.theater_list, name='theater_list'),
    path('success/', views.booking_success, name='booking_success'),
]