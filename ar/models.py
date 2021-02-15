from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(default='')
    url = models.CharField(max_length=100)


    def __str__(self):
        return self.title
