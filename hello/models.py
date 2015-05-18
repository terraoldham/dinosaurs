from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class InstagramPost(models.Model):
    url = models.TextField(default=''),
    tags = models.TextField(default=''),
    caption = models.TextField(default=''),
    username = models.TextField(default=''),
    full_name = models.TextField(default=''),
    likes = models.TextField(default=''),
    creation_date = models.TextField(default=''),
    location = models.TextField(default='')
