from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from .forms import DataForm
from .models import Data

# Create your views here.
def add_data(request):
	if request.method == 'POST':
		form = DataForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('Data added to DB')
	else:
		form = DataForm()
	return render(request, 'add_data.html', {'data_form':form})

def list_data(request):
	return render(request,'list_data.html',{
			'data': Data.objects.all()
		})

