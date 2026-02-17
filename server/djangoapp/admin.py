from django.contrib import admin
from .models import CarMake, CarModel

class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  

class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'description')
    inlines = [CarModelInline]

class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'make', 'type', 'year', 'price')
    list_filter = ('make', 'type', 'year')
    search_fields = ('name', 'make__name')

admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
