from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Products
from .modules.tokoscraper import tokopedia_main
from .modules.bukascraper import bukalapak_main

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