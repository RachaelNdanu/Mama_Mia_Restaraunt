from django.contrib import admin
from django.utils.html import format_html
from .models import Menu, Booking

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image_preview')
    search_fields = ('name', 'description')

    def image_preview(self, obj):
        if obj.image_url:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 4px;" />', obj.image_url)
        return "-"
    image_preview.short_description = 'Image'

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'guest_number', 'comment')
    search_fields = ('first_name', 'last_name', 'comment')
