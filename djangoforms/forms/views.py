from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView

# Create your views here.
def home(request):
	template = 'home.html'
	return render(request,'home.html',{})