from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, View
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from dj_tasks.models import ChecklistTemplate, TemplateStep, UserChecklist, UserChecklistStep

# Create your views here.
class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name = 'index.html'

class ChecklistTemplateListView(LoginRequiredMixin, ListView):
    """
    Displays a list of all checklist templates
    """
    model = ChecklistTemplate
    template_name = 'checklist_template_list.html'
    context_object_name = 'checklist_templates'

