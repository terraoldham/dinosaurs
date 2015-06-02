from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Greeting, InstagramPost
import os

def popular_posts():
		r = requests.get('https://api.instagram.com/v1/media/popular?client_id=015f71721d534f73afeec647c844105b')
		data = r.json()
		items = data.get('data')
		return items

def get_items():
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
		like_count = like_count,
		filter = item['filter']
	)
	return instagrampost