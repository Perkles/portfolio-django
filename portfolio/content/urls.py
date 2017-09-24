from content import views
from django.contrib import admin
from django.conf.urls import url , include

urlpatterns = [
    url(r'^$', views.home),
    url(r'^artigos/(?P<id_pagina_artigo>\d+)$', views.artigos),
    url(r'^portfolio/$', views.portfolio),
]