from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('intro/', views.Intro.as_view(), name="Intro"),
    path('library/', views.my_library.as_view(), name="my_library"),
    path('comments/', views.comments.as_view(), name="comments"),


]
