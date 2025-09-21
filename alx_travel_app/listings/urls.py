from django.urls import path
from . import views

urlpatterns = [
    #we'll add actual endpoints
    path('', views.api_overview, name='api-overview'),
]