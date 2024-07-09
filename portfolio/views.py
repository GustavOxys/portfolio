from django.http import HttpResponse
from django.views.generic import ListView
from .models import Skill
from django.shortcuts import render, get_object_or_404
from .models import Skill 

class Index(ListView):
    model = Skill
    template_name = 'portfolio/index.html'
    context_object_name = 'skills'

def skill_detail(request, slug):
    skill = get_object_or_404(Skill, slug=slug)
     
    return render(request, 'skill_detail.html', {'skill': skill,})

