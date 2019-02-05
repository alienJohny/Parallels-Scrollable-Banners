from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name="homepage"),
    url(r'upload/', views.upload, name="upload"),
]