from django.urls import path

from . import views

urlpatterns = [
    path('<str:username>', views.user, name="user"),
    path('notEnoughData/', views.notEnoughData, name="notEnoughData"),
    path('', views.index, name="index")
]
