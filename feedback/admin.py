from django.contrib import admin
from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'short_msg', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'message')
    ordering = ('-created_at',)
    def short_msg(self, obj):
        return (obj.message[:50] + '…') if len(obj.message) > 50 else obj.message
    short_msg.short_description = 'Сообщение'
