from django.urls import path
from .views import ChecklistTemplateDetailView, ChecklistTemplateListView, HomePage

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('checklist-templates/', ChecklistTemplateListView.as_view(), name="checklist_template_list"),
    path('checklist-templates/<int:pk>/', ChecklistTemplateDetailView.as_view(), name="checklist_template_detail"),
]
