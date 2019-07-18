from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^messages/?$', views.messages_post, name='messages_post'),
    url(r'^messages/(?P<hash>\w+)/?$', views.messages_get, name='messages_get')
]
