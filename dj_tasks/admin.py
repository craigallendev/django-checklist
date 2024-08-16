from django.contrib import admin
from .models import ChecklistTemplate, TemplateStep, UserChecklist, UserChecklistStep

@admin.register(ChecklistTemplate)
class ChecklistTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at')
    search_fields = ('name', 'description', 'created_by__username')
    list_filter = ('created_by', 'created_at',)

@admin.register(TemplateStep)
class TemplateStepAdmin(admin.ModelAdmin):
    list_display = ('template', 'step_int')
    search_fields = ('template__name', 'step_int')
    list_filter = ('template',)

@admin.register(UserChecklist)
class UserChecklistAdmin(admin.ModelAdmin):
    list_display = ('user', 'template', 'created_at', 'completed', 'completed_at')
    search_fields = ('user__username', 'template__name')
    list_filter = ('user', 'template', 'created_at', 'completed_at')

@admin.register(UserChecklistStep)
class UserChecklistStepAdmin(admin.ModelAdmin):
    list_display = ('user_checklist', 'template_step', 'completed')
    search_fields = ('user_checklist__user__username', 'template_step__template__name', 'template_step__step_int')
    list_filter = ('user_checklist', 'template_step', 'completed',)