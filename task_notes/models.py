from django.db import models
from dj_tasks.models import UserChecklistStep

# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    template_step = models.ForeignKey(template_step.UserChecklistStep)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title