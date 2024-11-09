from .models import UrlShortenerModel
from .utils import generate_short_url
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect, get_object_or_404
from django.core.validators import URLValidator


class UrlShortenerAPI(APIView):
    def post(self, request):
        try:
            original_url = request.data.get('original_url')
            
            if not original_url:
                return Response({'message': 'original_url is required'}, status=status.HTTP_400_BAD_REQUEST)    

            validator = URLValidator()
            try:
                validator(original_url)
            except:
                return Response({'success': False, 'message': 'Invalid URL'}, status=status.HTTP_400_BAD_REQUEST)

            url_instance = UrlShortenerModel.objects.filter(original_url=original_url).first()

            if url_instance:
                return Response({'message': f'https://sit.up.railway.app/{url_instance.short_url}'}, status=status.HTTP_201_CREATED)
            
            short_url = generate_short_url(original_url)

            UrlShortenerModel.objects.create(original_url=original_url, short_url=short_url)

            return Response({'message': f'https://sit.up.railway.app/{short_url}'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class RedirectAPI(APIView):
    def get(self, request, short_url):
        try:
            url = get_object_or_404(UrlShortenerModel, short_url=short_url)
        except UrlShortenerModel.MultipleObjectsReturned:
            return Response({'message': 'Multiple entries found for this short URL'}, status=status.HTTP_400_BAD_REQUEST)
        except UrlShortenerModel.DoesNotExist:
            return Response({'message': 'Short Url not found'}, status=status.HTTP_404_NOT_FOUND)
        return redirect(url.original_url)
        

