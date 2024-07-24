from django.contrib import admin
from .models import Skill, Project, About

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_class', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('first_name', )