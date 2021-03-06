from .scripts.scrapy.crawl_script import crawl_query
from .models import ESGModel

# Create your views here. Function taking request, and returns and output - 'action', called 'view' in django
#Normally 'template' what a user sees in django
from django.shortcuts import render
from django.http import HttpResponse
from uuid import uuid4
import threading

import logging

logger = logging.getLogger()

def company_input(request):
    event = threading.Event()

    def callback(result):
        event.set()

    key = 'company_query'
    if key in request.POST:
        logger.info('POST request received.')
        ESGModel.objects.all().delete()
        uid = str(uuid4())
        crawl_query(request.POST[key], "environmental", uid, callbacks=[callback])
        event.wait()
        try:
            item = ESGModel.objects.get(uid=uid)
            score_val = "{:.6f}".format(float(item.data)) #Rounding to 4 sf for score value
            return render(request, 'results.html', {'score':item.data})
        except:
            logger.error('item failed')

    return render(request, 'index.html')
