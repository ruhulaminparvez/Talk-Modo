from django.contrib import admin
from . models import Room, Message

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'content', 'date_added')
    list_filter = ('room', 'user')
    search_fields = ('content','room')

admin.site.register(Room)
admin.site.register(Message, MessageAdmin)
