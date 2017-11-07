from django.contrib import admin
from .models import Question


@admin.register(Question)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'date',)
    list_editable = ('description',)
