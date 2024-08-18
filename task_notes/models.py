from django.db import models
from django.contrib.auth.models import User
from dj_tasks.models import UserChecklistStep

# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    template_step = models.ForeignKey(UserChecklistStep, on_delete=models.CASCADE, related_name='related_notes')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title