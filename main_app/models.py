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
