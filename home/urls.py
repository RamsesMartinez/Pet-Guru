from django.conf.urls import url
from . import views
from .views import RegisterUser

app_name = 'home'

urlpatterns = [
    url(r'^$', views.index, name='inicio'),
    url(r'^user/$', views.user, name='usuario'),
    url(r'^nosotros/$', views.us, name='nosotros'),
    url(r'^reglamento/$', views.rules, name='reglamento'),
    url(r'^pregunta/(?P<id>[0-9]+)/$', views.question, name='pregunta'),
    url(r'^registro/$', RegisterUser.as_view(), name='register'),
    url(r'^logout/$', views.logout, name='logout'),
]
