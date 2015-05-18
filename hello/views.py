from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Greeting, InstagramPost
import os

# Create your views here.
def index(request):
	r = requests.get('https://api.instagram.com/v1/media/popular?client_id=015f71721d534f73afeec647c844105b')
	data = r.json()
	items = data.get('data') # data['data']
	item_id = 0 
	
	for i in items:
		instagrampost = InstagramPost(
			url = i['images']['standard_resolution']['url'],
			tags = i['tags'],
			caption = i['caption']['text'],
			username = i['user']['username'],
			full_name = i['user']['full_name'],
			likes = i['likes']['count'],
			creation_date = i['created_time'],
			location = i['location']['name']	
		)
		instagrampost.save()
		posts = instagrampost.objects.all()
		return render(request, 'home.html', {'posts': [posts]})

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

