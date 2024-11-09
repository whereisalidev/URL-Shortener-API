from django.db import models


class UrlShortenerModel(models.Model):
    original_url = models.TextField()
    short_url = models.TextField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.short_url} -> {self.original_url}"
    
