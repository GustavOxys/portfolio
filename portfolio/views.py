from django.http import HttpResponse
from django.views.generic import ListView
from .models import Habilidade

class Index(ListView):
    template_name = 'portfolio/index.html'
    queryset = Habilidade