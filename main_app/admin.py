from django.contrib import admin
from .models import Comment, File

# Register your models here.

admin.site.register(Comment)
admin.site.register(File)