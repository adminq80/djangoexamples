#urls.py

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^testbox/', include('testbox.urls')),
    url(r'^admin/', admin.site.urls),
]
##################################################
#testbox/urls.py

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
]
##################################################
#textbox/view.py

from django.http import HttpResponse

def index(request):
	return HttpResponse('Hello world.')
##################################################
