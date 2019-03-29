from django.conf.urls import url
from uwsgi_test import views

urlpatterns = [
    url(r'^uwsgi_test/$', views.uwsgi_test),
]
