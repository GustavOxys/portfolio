from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Skill
from django.shortcuts import render, get_object_or_404
from .models import Skill, Project, About
from datetime import date

class Index(ListView):
    model = Project
    template_name = 'portfolio/index.html'
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills'] = Skill.objects.all()
        about = About.objects.first()
        context['about'] = about
        context['age'] = self.calculate_age(about.date_of_birth)
        for project in context['projects']:
            project.skill_icons = [(skill.icon_class, skill) for skill in project.skills.all()]
        return context
    
    def calculate_age(self, birth_date):
        today = date.today()
        return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))


class SkillDetailView(DetailView):
    model = Skill
    template_name = 'portfolio/skill_detail.html'
    context_object_name = 'skill'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.filter(skills=self.object)
        return context
    

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'portfolio/project_detail.html'
    context_object_name = 'project'
    slug_field = 'name'
    slug_url_kwarg = 'name'