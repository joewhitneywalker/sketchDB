from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('intro/', views.Intro.as_view(), name="Intro"),
    path('library/', views.My_Library.as_view(), name="my_library"),
    path('comments/', views.Comments.as_view(), name="comments"),


]
