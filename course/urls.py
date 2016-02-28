import indexview
from django.conf.urls import url
urlpatterns = [

    url(r'^$',indexview.index),
]
