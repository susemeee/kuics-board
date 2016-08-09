from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.list, name='list'),
    url(r'^auth/$', views.auth, name='auth'),
    url(r'^auth/hello/$', views.auth_submit, name='auth_submit'),
    url(r'^auth/bye/$', views.auth_logout, name='auth_logout'),
    url(r'^add/$', views.add, name='add'),
    url(r'^add/submit/$', views.add_submit, name='add_submit'),
    url(r'^(?P<board_id>\d+)/$', views.view, name='view'),
    # url(r'^(?P<board_id>\d+)/update/$', views.update, name='update'),
    # url(r'^(?P<board_id>\d+)/update/submit/$', views.update_submit, name='update_submit'),
)
