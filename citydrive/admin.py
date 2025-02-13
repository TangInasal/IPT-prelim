from django.contrib import admin
from .models import Customer, Vehicle, Booking, Review

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'user_email', 'loyalty_points', 'country', 'language')
    search_fields = ('user__first_name', 'user__last_name', 'user__email', 'country', 'language')
    list_filter = ('country', 'language')

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = 'User Email'

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_type', 'transmission', 'fuel_type', 'location', 'price', 'availability')
    list_filter = ('vehicle_type', 'availability', 'transmission', 'fuel_type')
    search_fields = ('location', 'vehicle_type', 'transmission', 'fuel_type')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user_full_name', 'vehicle', 'pickup_date', 'dropoff_date', 'payment_status', 'booking_status')
    list_filter = ('booking_status', 'payment_status', 'pickup_date')
    search_fields = ('user__first_name', 'user__last_name', 'vehicle__vehicle_type', 'pickup_location')
    raw_id_fields = ('user', 'vehicle')

    def user_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    user_full_name.short_description = 'User Name'

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'vehicle', 'get_rating', 'comment_snippet')
    list_filter = ('vehicle__vehicle_type', 'rating')
    search_fields = ('user__user__first_name', 'user__user__last_name', 'comment', 'vehicle__vehicle_type')

    def customer_name(self, obj):
        return obj.user.get_full_name()
    customer_name.short_description = 'Customer Name'

    def get_rating(self, obj):
        return obj.get_rating_display()
    get_rating.short_description = 'Rating'

    def comment_snippet(self, obj):
        return obj.comment[:50] + '...' if len(obj.comment) > 50 else obj.comment
    comment_snippet.short_description = 'Comment'