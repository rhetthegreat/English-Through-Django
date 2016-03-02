from django.http import HttpResponse
from django.shortcuts import render
from models import *
def index(request):
    firstPage = Page.objects.all()[0]
    chapter=Chapter.objects.all()[0]
    topic = Topic.objects.all()[0]
    firstPage.wellOffset=(12-firstPage.wellWidth)/2
    return render(request,"index.html",{'page':firstPage,'chapter':chapter,'topic':topic})
def gettopic(request,topicid):
    firstPage = Page.objects.all()[0]
    chapter=Chapter.objects.all()[0]
    topic = Topic.objects.get(id=topicid)
    firstPage.wellOffset=(12-firstPage.wellWidth)/2
    return render(request,"index.html",{'page':firstPage,'chapter':chapter,'topic':topic})
