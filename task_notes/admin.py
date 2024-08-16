from django.contrib import admin
from .models import Notes

# Register your models here.
@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_on', 'updated_on', 'content')
    search_fields = ('name', 'description', 'created_by__username')
    list_filter = ('created_by', 'created_at',)

