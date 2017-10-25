from django.conf import settings
from django.conf.urls import url
from . import views

app_name='home'

urlpatterns = [
  url(r'^consultas/$', views.index, name='index.html'),    
  url(r'^nosotros/$', views.nosotros, name='nosotros.html'),
  url(r'^reglamento/$', views.reglamento, name='reglamento.html'),
]