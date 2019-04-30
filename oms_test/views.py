from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import logging
import random
import json


# Create your views here.
def reorder(request):
    logging.info('------------------------------------')
    logging.info(request)
    order_number = '100108776'
    order_number = '%s%s' % (order_number[0:-2], random.randrange(10, 99))
    logging.info(order_number)
    return JsonResponse({
        'order_id': '1',
        'order_number': order_number
    })
