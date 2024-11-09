from django.db import models


class UrlShortenerModel(models.Model):
    original_url = models.TextField()
    short_url = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
