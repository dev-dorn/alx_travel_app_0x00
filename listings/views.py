from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Admin Panel': '/admin/',
        'Swagger Documentation': '/swagger/',
        'Redoc Documentation': '/redoc/',
        'Listing API (Future)': '/api/listings',

    }
    return Response(api_urls)