from django.shortcuts import render
from django.http import HttpResponse
from instagram_api import popular_posts, get_items
import requests
from .models import Greeting, InstagramPost
import os

def instagramAPI(request):
	if request.method == "POST":
		popular_posts()
	return render(request, 'home.html')


def dino(request):
	for item in items:
		get_items(items)

	dino_page_posts = InstagramPost.objects.all().order_by('-id') 
	return render(request, 'dino.html', {'dino_page_posts': dino_page_posts}) #returns all of the dinoposts 
	

def filtered(request):
	for item in itmes: 
		get_items(items)

	filtered_posts =  InstagramPost.objects.filter(filter="Normal").filter(tag_text__icontains="nofilter")
	return render(request, 'filtered.html', {'filtered_posts': filtered_posts})  #returns posts that are contain a filter 
	

def db(request):

    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
    		

