from django.contrib import admin
from .models import Booking_History

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    search_fields = ('name', 'from_place', 'to_place', 'seat_no')
    list_display = ('name', 'from_place', 'to_place', 'booking_date', 'seat_no')
admin.site.register(Booking_History, BookAdmin)