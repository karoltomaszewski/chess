from django.urls import path

from . import views

urlpatterns = [
    path('<str:username>', views.user, name="user"),
    path('', views.index, name="index")#potem sie to zrobi
]
