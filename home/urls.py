from django.conf import settings
from django.conf.urls import url

from . import views

app_name='home'

urlpatterns = [
	url(r'^index/$', views.index, name='index'),    
    url(r'^$', views.nosotros, name='nosotros'),
    url(r'^reglamento/$', views.reglamento, name='reglamento'),
]