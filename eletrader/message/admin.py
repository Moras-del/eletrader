from django.contrib import admin

from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('user_from', 'user_to', 'order', 'content', 'post_date', 'is_active')
    list_filter = ('user_from', 'post_date', 'is_active')


# Register your models here.
