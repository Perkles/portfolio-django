from .views import Blog, Articles
from django.contrib import admin
from django.conf.urls import url

urlpatterns = [
    url(r'^$', Blog),
    url(r'^article(?P<id_pag>\d+)$',Articles),
]
