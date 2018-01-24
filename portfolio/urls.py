from .views import Portfolio
from django.contrib import admin
from django.conf.urls import url

urlpatterns = [
    url(r'^portfolio/', Portfolio),
]
