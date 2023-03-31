from django.db import models
from django.contrib.auth.models import User

class Page(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/')

class Message(models.Model):
    user_from = models.ForeignKey(User, on_delete=models.CASCADE,related_name="user_from")
    user_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_to")
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()




