from django.http import HttpResponse
from django.views.generic import ListView
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


def skill_detail(request, slug):
    skill = get_object_or_404(Skill, slug=slug)
     
    return render(request, 'portfolio/skill_detail.html', {'skill': skill,})

