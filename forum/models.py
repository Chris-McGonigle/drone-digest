from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Class to generate top level subject heading

class Topic(models.Model):
    subject = models.CharField(max_length=250)

    def __str__(self):
        return self.name
        

# Class to create unique threads

class Thread(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Class to create individual user posts      

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
