from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post

def index(request):
	context = {'posts': Post.objects.all()}
	return render(request, 'testbox/index.html', context)

def add(request):
	Post(body='Hello world.').save()
	return HttpResponseRedirect('/testbox/')