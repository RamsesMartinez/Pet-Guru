from django.conf.urls import include, url
from . import views

app_name='chat'

urlpatterns = (
    url(r'^room/(?P<label>\w+)/$', views.chat_room, name='chat_room'),
)