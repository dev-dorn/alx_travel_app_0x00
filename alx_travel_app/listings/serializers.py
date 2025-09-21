from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Listing, Booking, Review

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class ListingSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    
    class Meta:
        model = Listing
        fields = '__all__'
        read_only_fields = ['owner', 'created_at', 'updated_at']

class BookingSerializer(serializers.ModelSerializer):
    guest = UserSerializer(read_only=True)
    listing = ListingSerializer(read_only=True)
    listing_id = serializers.PrimaryKeyRelatedField(
        queryset=Listing.objects.all(), 
        source='listing', 
        write_only=True
    )
    
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['guest', 'total_price', 'created_at', 'updated_at']

class ReviewSerializer(serializers.ModelSerializer):
    guest = UserSerializer(read_only=True)
    listing = ListingSerializer(read_only=True)
    listing_id = serializers.PrimaryKeyRelatedField(
        queryset=Listing.objects.all(), 
        source='listing', 
        write_only=True
    )
    
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['guest', 'created_at', 'updated_at']