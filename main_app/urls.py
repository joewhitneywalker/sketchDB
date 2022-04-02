from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('intro/', views.Intro.as_view(), name="Intro"),

]
