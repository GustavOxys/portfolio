from django.urls import path
from .views import Index, SkillDetailView, ProjectDetailView
from . import views



app_name = 'portfolio'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('skills/<slug:slug>/', SkillDetailView.as_view(), name='skill_detail'),
    ]
