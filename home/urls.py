from django.conf.urls import url
from django.contrib import admin
from .views import homePageView

urlpatterns = [
    url('', homePageView, name='home')
]
