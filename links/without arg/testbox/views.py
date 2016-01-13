from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

def index(request):
	context = {'test': 'yey'}
	return render(request, 'testbox/index.html', context)

def test(request):
	return HttpResponse('Hi there.')