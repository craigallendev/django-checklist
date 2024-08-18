from django.contrib import admin
from .models import Notes

# Register your models here.
@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',  'created_on', 'updated_on', 'content')
    search_fields = ('author', 'title', 'created_on')
    list_filter = ('author', 'created_on')

