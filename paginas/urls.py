from django.contrib import admin
from django.urls import path
from .views import IndexView


urlpatterns = [
    path("home/", IndexView.as_view(), name="index")
]
