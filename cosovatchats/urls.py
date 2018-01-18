from django.conf.urls import url
from cosovatchats import views

urlpatterns = [
    url(r'^cosovatchats/$', views.cosovatchat_list),
    url(r'^cosovatchats/(?P<pk>[0-9]+)/$', views.cosovatchat_detail),
]