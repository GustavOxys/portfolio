from django.urls import path
from .views import Index
from . import views



app_name = 'portfolio'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('skills/<slug:slug>/', views.skill_detail, name='skill_detail'),

    ]
