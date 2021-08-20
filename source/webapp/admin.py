from django.contrib import admin
from webapp.models import (
    Image,
    Advert
)


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'phone_number', 'created_at']
    list_filter = ['author']
    search_fields = ['author']
    fields = ['id', 'author', 'description', 'phone_number', 'created_at']
    readonly_fields = ['id', 'created_at']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'advert', 'image']
    list_filter = ['advert']
    search_fields = ['advert']
    fields = ['id', 'image', 'advert']
    readonly_fields = ['id']