from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Greeting, InstagramPost
import os

# Create your views here.
def index(request):

    if request.method == "POST":
		r = requests.get('https://api.instagram.com/v1/media/popular?client_id=015f71721d534f73afeec647c844105b')
		data = r.json()
		items = data.get('data') # data['data']
	
		for item in items:
			caption = item['caption']['text'] if item['caption'] else None
			creation_date = item['caption']['created_time'] if item['caption'] else None
			like_count = item['likes']['count'] if item['likes'] else None
			instagrampost = InstagramPost.objects.create(
				photo_url = item['images']['standard_resolution']['url'],
				tag_text = item['tags'],
				caption = caption,
				creation_date = creation_date,
				user_name = item['user']['username'],
				fullname = item['user']['full_name'],
				like_count = item['likes']['count'],	
			)
	    
		dino_page_posts = InstagramPost.objects.order_by('-id')[:10]
		return render(request, 'dino.html', {'dino_page_posts': dino_page_posts})
		
    else: 
		return render(request, 'home.html')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
    	

