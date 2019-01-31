from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

import logging


# Create your views here.
def fun_cat(request):
    logging.debug(request.POST)
    logging.debug(request.GET)

    return HttpResponse(request.GET.get('echostr'))
