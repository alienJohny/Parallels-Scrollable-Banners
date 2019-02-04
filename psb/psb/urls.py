from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'get', include('get.urls')),
    url(r'^$', include('homepage.urls'))
]
