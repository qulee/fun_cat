"""pic_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from pic_site import views
from pic_site import urls as siteURLConf
from wx_test import views as funcat
from uwsgi_test import urls as uwsgi_url
from oms_test import urls as oms_test


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^pic_site/', include(siteURLConf)),
    url(r'^fun_cat/', funcat.fun_cat),
    url(r'^uwsgi/', include(uwsgi_url)),
    url(r'^oms_test/', include(oms_test)),
]
