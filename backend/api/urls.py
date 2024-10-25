from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='index'),
    path('room/<str:pk>/', views.room, name='room'),
]