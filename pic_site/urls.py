from django.conf.urls import url
from pic_site import views

urlpatterns = [
    url(r'^tag_list/', views.tag_list),
    url(r'^img_upload/', views.img_upload),
    url(r'^success/', views.success),
    url(r'^test/$', views.just_test),
    url(r'^test/Order/Status/Update', views.t_update),
    url(r'^test/Order/Add', views.t_add),
    url(r'^test/Accounts', views.t_accounts),

]
