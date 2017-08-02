from django.conf.urls import url
from scheduler import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
]
