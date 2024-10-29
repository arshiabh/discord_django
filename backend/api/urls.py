from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.LoginPage, name='login'),

    path('', views.home, name='index'),
    path('room/<str:pk>/', views.room, name='room'),

    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>', views.UpdateRoom, name='update-room'),
    path('delete-room/<str:pk>', views.DeleteRoom, name='delete-room'),
]