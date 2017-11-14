from django.contrib import admin
from .models import Room, Message

# Register your models here.

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'label',)
    list_editable = ('label',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('room', 'handle', 'message', 'timestamp',)    