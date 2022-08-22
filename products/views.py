import csv
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Products
from .modules.tokoscraper import tokopedia_main
from .modules.bukascraper import bukalapak_main

def tokopedia_download(request):
    if request.method == 'POST':
        total = request.POST['amount']
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': 'attachment; filename="tokoscraper_tokopedia.csv"'},
        )
        pdatas = tokopedia_main(total)
        writer = csv.writer(response)
        writer.writerow(['Name', 'Price', 'Store Name', 'Rating', 'Review', 'URL'])
        for data in pdatas:
            writer.writerow([data['name'], data['price'], data['shop']['name'], data['rating'], data['countReview'], data['url']])
        return response

def bukalapak_download(request):
    if request.method == 'POST':
        total = request.POST['amount']
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': 'attachment; filename="tokoscraper_bukalapak.csv"'},
        )
        pdatas = bukalapak_main(total)
        writer = csv.writer(response)
        writer.writerow(['Name', 'Price', 'Store Name', 'Rating', 'Review', 'URL', 'Description'])
        for data in pdatas:
            writer.writerow([data['name'], data['price'], data['store']['name'], data['rating']['average_rate'], data['rating']['user_count'], data['url'], data['description']])
        return response

def tokopedia(request):
    if request.method == 'GET':
        methid = 'GET'
        template = loader.get_template('pages/tokopedia.html')
        context = {
            'methid': methid,
        }
        return HttpResponse(template.render(context, request))

    elif request.method == 'POST':
        total = request.POST['amount']
        methid = 'POST'
        pdatas = tokopedia_main(total)
        template = loader.get_template('pages/tokopedia.html')
        context = {
            'pdatas': pdatas,
            'total': total,
            'methid': methid,
        }
        return HttpResponse(template.render(context, request))

def bukalapak(request):
    if request.method == 'GET':
        methid = 'GET'
        template = loader.get_template('pages/bukalapak.html')
        context = {
            'methid': methid,
        }
        return HttpResponse(template.render(context, request))

    elif request.method == 'POST':
        total = request.POST['amount']
        methid = 'POST'
        pdatas = bukalapak_main(total)
        template = loader.get_template('pages/bukalapak.html')
        context = {
            'pdatas': pdatas,
            'total': total,
            'methid': methid,
        }
        return HttpResponse(template.render(context, request))

def index(request):
    if request.method == 'GET':
        return HttpResponseRedirect(reverse('tokopedia'))