from django.conf.urls import url

from . import views

app_name = 'appName'

urlpatterns = [
    url(r'^$', views.index),
    url(r'^test/$', views.test,name = 'methodName'),
]