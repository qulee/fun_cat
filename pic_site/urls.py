from django.conf.urls import url
from pic_site import views

urlpatterns = [
    url(r'^tag_list/', views.tag_list),
    url(r'^img_upload/', views.img_upload),
    url(r'^success/', views.success),
    url(r'^test/', views.just_test),


]
