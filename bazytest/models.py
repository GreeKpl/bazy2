from django.db import models

# Create your models here.

class User(models.Model):
  name = models.CharField(max_length=30)
  join_date = models.DateTimeField()

class Post(models.Model):
  title = models.CharField(max_length=30)
  content = models.TextField()
  author = models.ForeignKey(User)
  date = models.DateTimeField()
