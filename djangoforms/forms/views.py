from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from .forms import NameForm
from .forms import CarForm
from .models import Car

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

def add_car(request):
	if request.method == 'POST':
		form = CarForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('car added to the database')
	else:
		form  = CarForm()

	return render(request,'add_car.html', {'car_form':form})

def car_list(request):
	return render(request,'car_list.html',{
			'cars':Car.objects.all()
		})

def car_details(request,car_billing_number):
	return render(request,'car_details.html',{
			'car':Car.objects.get(billing_number = car_billing_number)
		})

