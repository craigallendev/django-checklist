from dj_tasks.models import ChecklistTemplate


def navbar_checklist_templates(request):
    return {"navbar_checklist_templates": ChecklistTemplate.objects.all()}