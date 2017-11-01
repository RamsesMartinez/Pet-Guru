from django.contrib import admin
from .models import Question


@admin.register(Question)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('id', 'species', 'question', 'date',)
    list_editable = ('question',)
