from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'year', 'price', 'type')
    search_fields = ('brand', 'model')
    list_filter = ('type', 'year')
