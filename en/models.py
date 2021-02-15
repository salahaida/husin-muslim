from django.db import models


# Create your models here.

class PostEN(models.Model):
    title_en = models.CharField(max_length=50)
    content_en = models.TextField(default='')
    url_en = models.CharField(max_length=100)



    def __str__(self):
        return self.title_en
