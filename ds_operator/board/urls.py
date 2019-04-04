from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:board_id>',views.detail, name="detail"),
    path('post/',views.post, name='post'),
    path('show/', views.show, name='show'),
    #path('photo/', views.photo, name="photo"),
]
