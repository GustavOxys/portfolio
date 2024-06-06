from django.http import HttpResponse
from django.views import View

class Index(View):
    def get(self, request):
        # Retorna uma resposta HTTP com um conteúdo simples
        return HttpResponse("Olá, mundo!")