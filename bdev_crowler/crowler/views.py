from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import DataCollected
from django.http import HttpResponse, JsonResponse


def crawler_free_images(request, search):
    data_collected=[]
    for index in range(11):
        response = requests.get(f'https://www.freeimages.com/search/{search}/{index if index != 1 else ""}')
        soup = BeautifulSoup(response.text, 'html.parser')
        figures = soup.findAll('figure', class_='grid-figure')
        for fig in figures:
            img = fig.find('img')
            img_url = img.attrs['src']
            data = DataCollected.objects.create(title=search, url=img_url)
            data.save()
            data_collected.append(img_url)
    return JsonResponse(data_collected, safe=False)


def crawl_through_request(request, search):
    data_collected = []
    for index in range(10):
        response = requests.get(f'https://geoapi.freeimages.com/istock/search/?phrase={search}&page={index}&page_size=100&graphical_styles=photography&lang=en-US')
        content = response.json()['data']['results']
        for image in content:
            url = image['display_sizes'][0]['uri']
            data = DataCollected.objects.create(title=search, url=url)
            data.save()
            data_collected.append(url)
    return JsonResponse(data_collected, safe=False)

