from django.conf.urls import url
from oms_test import views

urlpatterns = [
    url(r'reorder/$', views.reorder),

]
