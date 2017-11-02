from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^bus/', views.bus, name = 'bus'),
	url(r'^hotel/', views.hotel, name = 'hotel'),
]