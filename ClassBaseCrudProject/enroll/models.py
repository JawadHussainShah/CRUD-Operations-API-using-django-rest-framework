import email
from pyexpat import model
from unicodedata import name
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=15)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=15)