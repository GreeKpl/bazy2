from django.db import models

# Create your models here.

class User(models.Model):
  login = models.CharField(max_length=30)
  city = models.CharField(max_length=30)
  create_date = models.DateTimeField()
  age = models.IntegerField()
  is_woman = models.BooleanField()
  def __unicode__(self):
    return self.login + " (" + str(self.age) + ") " + ("K" if self.is_woman else "M")

class Thread(models.Model):
  title = models.CharField(max_length=30)
  create_date = models.DateTimeField()
  user = models.ForeignKey(User)
  def __unicode__(self):
    return '"' + self.title + '" by ' + self.user.login

class Post(models.Model):
  thread = models.ForeignKey(Thread)
  content = models.TextField()
  date = models.DateTimeField()
  author = models.ForeignKey(User)
  location = models.CharField(max_length=30)
  def __unicode__(self):
    return "post #" + self.id + " by " + self.author.login
