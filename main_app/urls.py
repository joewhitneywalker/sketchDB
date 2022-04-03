from django.urls import path
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('intro/', views.Intro.as_view(), name="Intro"),
    path('library/', views.My_Library.as_view(), name="my_library"),
    path('comments/', views.Comments.as_view(), name="comments"),
    path('upload/', views.upload, name="upload"),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)