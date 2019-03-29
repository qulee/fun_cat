from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

def uwsgi_test(request):
    return HttpResponse('quleess')