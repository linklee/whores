from whores_app import views
from django.conf.urls import include, url
from django.contrib import admin

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
]