from django.db import models

# Create your models here.
# class user_register(models.Model):
#     name=models.CharField(max_length=50)
#     email=models.CharField(max_length=50,unique=True)
#     password=models.CharField(max_length=50)
#     confirm_password=models.CharField(max_length=50)
class comment(models.Model):
    name=models.CharField(max_length=100)
    text=models.CharField(max_length=5000)