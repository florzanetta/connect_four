from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_id>[0-9]+)/$', views.play, name='play'),
    url(r'^next/$', views.my_turn, name='my_turn')
]
