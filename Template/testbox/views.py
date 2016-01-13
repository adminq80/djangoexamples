from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

def index(request):
	context = {'test': 'Hello world.'}
	return render(request, 'testbox/index.html', context)