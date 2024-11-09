from .models import UrlShortenerModel
from rest_framework import serializers

class UrlShortenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlShortenerModel
        fields = ['original_url', ]