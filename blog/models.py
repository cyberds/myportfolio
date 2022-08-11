from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class blog(models.Model):
    title = models.CharField(max_length = 1000)
    slug = models.SlugField(unique=True, max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_on = models.DateField(default=timezone.now)
    published = models.BooleanField(default=True)
    like = models.IntegerField(default='1')
    body = models.TextField(max_length=8000)
    thumbnail = models.ImageField(upload_to='blog_pictures/thumbnails')
    image = models.ImageField(upload_to="blog_pictures")


