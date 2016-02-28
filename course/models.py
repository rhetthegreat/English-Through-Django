from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
# Create your models here.
class Page(models.Model):
    title=models.CharField(max_length=50)
class Content(models.Model):
    body=models.TextField()
class Topic(models.Model):
    name = models.CharField(max_length=200)
    contents = models.ManytoManyField(Content)
class Chapter(models.Model):
    name = models.CharField(max_length=200)
    position=models.IntegerField()
    topics = models.ManytoManyField(Topic)
class PageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Page,PageAdmin)
