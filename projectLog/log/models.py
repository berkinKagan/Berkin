from datetime import date, datetime
from sqlite3 import Date
from turtle import title
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(default=datetime.now, blank= True)
    body = models.CharField(max_length=10000000000000000000000)
    
    