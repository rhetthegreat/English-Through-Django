from django.http import HttpResponse
from django.shortcuts import render
from models import *
def index(request):
    firstPage = Page.objects.get()
    return render(request,"index.html",{'page':firstPage})
