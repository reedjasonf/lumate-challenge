from django.conf.urls import patterns, url
from guestbook import views

urlpatterns = patterns('',
    url(r'^$', views.index, {'signed_val': False}, name='index'),
    url(r'^/signed/$', views.index, {'signed_val': True}, name='signed_guestbook'),
    url(r'^/view/$', views.view, name='view'),
    url(r'^/sign/$', views.sign, name='sign'),
)
