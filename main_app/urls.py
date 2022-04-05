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
    path('files/', views.file_list, name="file_list"),
    path('files/upload', views.file_upload, name="file_upload"),
    path('class/files/', views.FileListView.as_view(), name='class_file_list'),#for class based file list
    path('class/files/upload/', views.UploadFileView.as_view(), name='class_file_upload'),
    




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)