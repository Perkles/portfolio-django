from django.contrib import admin
from django.conf.urls import url , include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('content.urls')),
    url(r'^portfolio', include('portfolio_page.urls')),
    url(r'^sobremim', include('about_me.urls')),


]
