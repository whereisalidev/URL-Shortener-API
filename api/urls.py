from django.urls import path
from . views import UrlShortenerAPI, RedirectAPI

urlpatterns = [
    path('api/shorten', UrlShortenerAPI.as_view()),
    path('<str:short_url>', RedirectAPI.as_view())
]
