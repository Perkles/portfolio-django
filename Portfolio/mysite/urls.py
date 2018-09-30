from django.contrib import admin
from django.conf.urls import url , include

from django.conf import settings # import to make ImageField importation path work
from django.conf.urls.static import static # import to make ImageField importation path work

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('blog.urls')),
    url(r'^', include('portfolio.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #The path url
