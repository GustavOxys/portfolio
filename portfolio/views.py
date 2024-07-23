from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Skill
from django.shortcuts import render, get_object_or_404
from .models import Skill, Project

class Index(ListView):
    model = Project
    template_name = 'portfolio/index.html'
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills'] = Skill.objects.all()
        for project in context['projects']:
            project.skill_icons = [skill.icon_class for skill in project.skills.all()]
        return context




class SkillDetailView(DetailView):
    model = Skill
    template_name = 'portfolio/skill_detail.html'
    context_object_name = 'skill'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.filter(skills=self.object)
        return context