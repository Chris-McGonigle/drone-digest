from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """
    Class to generate top level subject heading
    """

    subject = models.CharField(max_length=250)

    def __str__(self):
        return self.subject


class Thread(models.Model):
    """
    Class to create unique threads
    """

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    droners = models.ManyToManyField(User, related_name="droners", blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Class to create individual user posts
    """

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return self.body[0:50]
