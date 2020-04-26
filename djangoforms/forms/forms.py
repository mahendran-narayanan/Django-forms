from django import forms
from .models import Car
from django.forms import ModelForm

class NameForm(forms.Form):
	your_name = forms.CharField(label='Your Name',max_length =100)

class CarForm(ModelForm):
	class Meta:
		model = Car
		exclude = ()