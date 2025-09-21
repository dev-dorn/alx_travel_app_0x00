from django.contrib import admin
from .models import Listing, Booking, Review

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ['title', 'city', 'country', 'property_type', 'price_per_night', 'is_available']
    list_filter = ['property_type', 'city', 'country', 'is_available']
    search_fields = ['title', 'description', 'address', 'city']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'listing', 'guest', 'check_in_date', 'check_out_date', 'status']
    list_filter = ['status', 'check_in_date', 'check_out_date']
    search_fields = ['listing__title', 'guest__username']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['listing', 'guest', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['listing__title', 'guest__username', 'comment']