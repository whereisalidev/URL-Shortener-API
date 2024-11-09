from django.urls import path
from . views import API

urlpatterns = [
    path('shorten', API.as_view())
]
