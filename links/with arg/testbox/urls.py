from django.conf.urls import url

from . import views

app_name = 'appName'

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<id>[0-9]+)/test/$', views.test,name = 'methodName'),
]