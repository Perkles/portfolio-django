from portfolio_page import views
from django.contrib import admin
from django.conf.urls import url

urlpatterns = [
    url(r'^', views.portfolio_pagina),
]