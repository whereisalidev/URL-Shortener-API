from .models import UrlShortenerModel
from .utils import generate_short_url
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect, get_object_or_404


class UrlShortenerAPI(APIView):
    def post(self, request):
        original_url = request.data.get('original_url')

        if not original_url:
            return Response({'message': 'original_url is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        short_url = generate_short_url(original_url)
        print('yes')

        UrlShortenerModel.objects.create(original_url=original_url, short_url=short_url)


        return Response({'message': f'http://127.0.0.1:8000/{short_url}'}, status=status.HTTP_201_CREATED)




class RedirectAPI(APIView):
    def get(self, request, short_url):
        try:
            url = get_object_or_404(UrlShortenerModel, short_url=short_url)
        except UrlShortenerModel.MultipleObjectsReturned:
            return Response({'message': 'Multiple entries found for this short URL'}, status=status.HTTP_400_BAD_REQUEST)
        except UrlShortenerModel.DoesNotExist:
            return Response({'message': 'Short Url not found'}, status=status.HTTP_404_NOT_FOUND)
        return redirect(url.original_url)
        

