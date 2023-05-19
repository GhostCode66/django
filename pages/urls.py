# Pages/urls.py

from django.urls import path

from .views import homepageview


urlpatterns = [
    path("", homepageview, name="home")
]
