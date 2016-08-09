"""kuicsboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.shortcuts import redirect
from board import urls as board_urls


def board_root_view(request):
    return redirect('board:list')

urlpatterns = [
    url(r'^!/administer/', include(admin.site.urls)),
    url(r'^board/', include(board_urls, namespace='board')),
    url(r'^$', board_root_view)
]
