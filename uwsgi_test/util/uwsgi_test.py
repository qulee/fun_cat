from django.http import HttpResponse, HttpResponseRedirect, JsonResponse


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b"Hello World"]
