from django.shortcuts import render
from django.http import HttpResponse
from .forms import TestForm

def index(request):
	context = {'form': TestForm()}
	return render(request, 'testbox/index.html', context)

def test(request):
	if request.method == 'POST':
		form = TestForm(request.POST)
		if form.is_valid():
			return HttpResponse(request.POST.get('post'))
		else:
			HttpResponse('Form is not valid.')
	else:	
		HttpResponse('Request method is not POST.')