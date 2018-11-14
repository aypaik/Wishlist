from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/dashboard', views.dashboard),
    url(r'^/add$', views.add),
    url(r'^/create', views.create),
    url(r'^/removefromlist/(?P<id>\d+$)', views.removefromlist),
    url(r'^/addtolist/(?P<id>\d+$)', views.addtolist),
    url(r'^/show/(?P<id>\d+$)', views.show),
]
