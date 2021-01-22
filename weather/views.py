from django.shortcuts import render, redirect
import requests
from .models import City
from .forms import CityForm
from django.contrib import messages

# Create your views here.

def homeView(request):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=b3b0d1d14cf371b4eccf0c20c0d13dca'
	city = City.objects.all()
	weather_cities = []
	try:
		for i in city:
			city_weather = requests.get(url.format(i)).json() #request the API data and convert the JSON to Python data types

			weather = {
			    'city' : i,
			    'temperature' : city_weather['main']['temp'],
			    'description' : city_weather['weather'][0]['description'],
			    'icon' : city_weather['weather'][0]['icon']
			}

			weather_cities.append(weather)
	except:
		messages.info(request, 'Three credits remain in your account.')

	if request.method == 'POST':
		form = CityForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			messages.add_message(request, messages.INFO, 'Hello world.')
	else:
		form = CityForm()

	context = {'weather_cities':weather_cities,'form':form}
	return render(request, 'home.html', context) #returns the index.html template
