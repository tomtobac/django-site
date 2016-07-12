from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey('auth.User')
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    draft = models.BooleanField(default=True)
    tag = models.ManyToManyField(Tag, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['published_date']
