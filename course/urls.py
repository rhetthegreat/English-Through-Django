import indexview
from django.conf.urls import url
urlpatterns = [

    url(r'^$',indexview.index),
    url(r'^topic/(?P<topicid>[0-9]{0,4})/$',indexview.gettopic)
]
