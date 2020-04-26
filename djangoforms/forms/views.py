from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView

from django.http import HttpResponseRedirect
from .forms import NameForm

# Create your views here.
def get_name(request):
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('thanks/')
	else:
		form = NameForm()
	return render(request, 'name.html', {'form':form})

def home(request):
	template = 'home.html'
	return render(request,'home.html',{})

def thanks(request):
	return HttpResponse("Data received")