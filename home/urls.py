from django.conf import settings
from django.conf.urls import url, include
from . import views

app_name='home'

urlpatterns = [
  url(r'^$', views.index, name='inicio'),    
  url(r'^nosotros/$', views.nosotros, name='nosotros'),
  url(r'^reglamento/$', views.reglamento, name='reglamento'),
  url(r'^pregunta/$', views.question, name='single-question'),
]