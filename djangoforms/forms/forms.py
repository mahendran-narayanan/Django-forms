from django import forms
from .models import Car,Data
from django.forms import ModelForm

class DataForm(ModelForm):
	class Meta:
		model = Data
		exclude = ()


class CarForm(ModelForm):
	class Meta:
		model = Car
		exclude = ()