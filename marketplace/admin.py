from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created', 'order_type', 'item_price', 'quantity')
    list_filter = ('owner', 'created', 'order_type')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

