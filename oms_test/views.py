from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import logging
import random
import json


# Create your views here.
def reorder(request):
    order_number = request.POST.get('order_number')
    order_number = '%s%s' % (order_number[0:-2], random.random(10, 99))
    return HttpResponse(json.dumps({
        'order_id': '1',
        'order_number': order_number
    }))
