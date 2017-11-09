from django.contrib import admin
from .models import Question, Bovine, Porcine, Horse, Ovine, Goat, Rabbit


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'date',)
    list_editable = ('description',)


@admin.register(Bovine)
class BovineAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')


@admin.register(Porcine)
class BovineAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')


@admin.register(Horse)
class BovineAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')


@admin.register(Ovine)
class BovineAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')


@admin.register(Goat)
class BovineAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')


@admin.register(Rabbit)
class BovineAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')

