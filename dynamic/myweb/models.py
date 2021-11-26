from django.db import models

# Create your models here.
from requests import request


class destination(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='image')
    desc=models.TextField(max_length=500)


