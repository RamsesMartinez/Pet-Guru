from django.conf import settings
from django.conf.urls import url, include
from . import views
from .views import RegisterUser

app_name='home'

urlpatterns = [

  url(r'^$', views.index, name='inicio'),    
  url(r'^user/$', views.user, name='usuario'),
  url(r'^nosotros/$', views.nosotros, name='nosotros'),
  url(r'^reglamento/$', views.reglamento, name='reglamento'),
  url(r'^pregunta/(?P<id>[0-9]+)/$', views.pregunta, name='pregunta'),
  url(r'^registro/$', RegisterUser.as_view(), name='register'),
  url(r'^logout/$', views.logout, name='logout'),
]