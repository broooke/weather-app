from django import forms
from .models import City
from django.forms import TextInput

class CityForm(forms.ModelForm):
	class Meta:
		model = City
		fields = ['name']
		widgets = {
            'name': TextInput(attrs={'class' : 'form-control', 'placeholder' : 'City Name'}),
        } #updates the input class to have the correct Bulma class and placeholder

