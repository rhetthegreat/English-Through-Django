from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
# Create your models here.
class Page(models.Model):
    title=models.CharField(max_length=50)
class Content(models.Model):
    body=models.TextField()
    header = models.TextField(blank=True)
    footer = models.TextField(blank=True)
    name=models.CharField(max_length=200)
    def __unicode__(self):
        return self.name
class Topic(models.Model):
    name = models.CharField(max_length=200)
    header = models.TextField(blank=True)
    footer = models.TextField(blank=True)
    contents =  models.ManyToManyField(Content,blank=True)
    def __unicode__(self):
        return self.name
class Chapter(models.Model):
    name = models.CharField(max_length=200)
    header = models.TextField(blank=True)
    footer = models.TextField(blank=True)
    position=models.IntegerField()
    topics = models.ManyToManyField(Topic,blank=True)
    def __unicode__(self):
        return self.name
class PageAdmin(admin.ModelAdmin):
    pass
class ChapterAdmin(admin.ModelAdmin):
    pass
class ContentAdmin(admin.ModelAdmin):
    pass
class TopicAdmin(admin.ModelAdmin):
    pass
admin.site.register(Chapter,ChapterAdmin)
admin.site.register(Topic,TopicAdmin)
admin.site.register(Content,ContentAdmin)
admin.site.register(Page,PageAdmin)
