from django.contrib import admin
from .models import Item, Order

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    list_filter = ('name', 'price')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('get_items', 'total_price')

    def get_items(self, obj):
        return ', '.join([
            items.name for items
            in obj.items.all()])
    get_items.short_description = 'Товары'

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.total_price = obj.calculate_total_price()
        obj.save()