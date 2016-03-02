from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Image(models.Model):
    image = models.ImageField(blank=True,null=True)
    name=models.CharField(max_length=200)
    caption=models.CharField(max_length=200)
    position=models.IntegerField()
    def __unicode__(self):
        return self.name
class Page(models.Model):
    title=models.CharField(max_length=50)
    wellWidth=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(12)])
    contentWidth = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(12)])
    imageWidth=models.IntegerField(validators=[MaxValueValidator(12)])
    wellOffset=models.IntegerField(validators=[MaxValueValidator(12)])
class Content(models.Model):
    body=models.TextField()
    header = models.TextField(blank=True)
    footer = models.TextField(blank=True)
    name=models.CharField(max_length=200)
    images=models.ManyToManyField(Image,blank=True)
    reading = models.FileField(blank=True,null=True)
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

class ImageAdmin(admin.ModelAdmin):
    pass
class PageAdmin(admin.ModelAdmin):
    pass
class ChapterAdmin(admin.ModelAdmin):
    pass
class ContentAdmin(admin.ModelAdmin):
    pass
class TopicAdmin(admin.ModelAdmin):
    pass
admin.site.register(Image,ImageAdmin)
admin.site.register(Chapter,ChapterAdmin)
admin.site.register(Topic,TopicAdmin)
admin.site.register(Content,ContentAdmin)
admin.site.register(Page,PageAdmin)
