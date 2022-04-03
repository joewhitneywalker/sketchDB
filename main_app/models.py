from django.db import models

class Comment(models.Model):
    body_text = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

     
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at'] #try using minus to get descending 


# Create your models here.

class File(models.Model):
    file_name = models.CharField(max_length=5)
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    pdf = models.FileField(upload_to='files/pdfs')#should this actually be the name of by db?
    season = models.CharField(max_length=4, default='FA20', editable=True)
    category = models.CharField(max_length=25, default='OUTERWEAR', editable=True)
    comments = models.CharField(max_length=5000, default="COMMENTS REQUIRED", editable=True)

    def __str__(self):
        return self.file_name
