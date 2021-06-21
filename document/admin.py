from django.contrib import admin

from .models import Document, History


@admin.register(Document)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'mime_type', 'created', 'updated', 'actived')

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('action', 'start_hour', 'end_hour', 'created')