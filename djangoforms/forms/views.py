from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from .forms import CarForm,DataForm
from .models import Car,Data

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

