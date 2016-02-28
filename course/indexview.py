from django.http import HttpResponse
from django.shortcuts import render
from models import *
def index(request):
    firstPage = Page.objects.all()[0]
    chapter=Chapter.objects.all()[0]
    topic = Topic.objects.all()[0]
    return render(request,"index.html",{'page':firstPage,'chapter':chapter,'topic':topic})
