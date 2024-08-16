from django.db import models
from django.contrib.auth.models import User

class ChecklistTemplate(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class TemplateStep(models.Model):
    template = models.ForeignKey(ChecklistTemplate, on_delete=models.CASCADE)
    step_int = models.CharField(max_length=100, default='Untitled Step')
    description = models.TextField()
    code = models.TextField()
    image = models.ImageField(upload_to='template_images/', blank=True, null=True)

    def __str__(self):
        return f'{self.template.name} - Step {self.step_int}'
    
class UserChecklist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    template = models.ForeignKey(ChecklistTemplate, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} - {self.template.name}'
    
class UserChecklistStep(models.Model):
    user_checklist = models.ForeignKey(UserChecklist, on_delete=models.CASCADE)
    template_step = models.ForeignKey(TemplateStep, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user_checklist.user.username} - {self.template_step.template.name} - Step {self.template_step.step_int}'



