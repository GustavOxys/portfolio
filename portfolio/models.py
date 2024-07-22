from django.db import models
from django.utils.text import slugify

class Sobre(models.Model):
    primeiro_nome = models.CharField(max_length=10)
    sobrenome = models.CharField(max_length=15)
    ano_nascimento = models.DateField()
    texto = models.TextField()
    idade = models.IntegerField()

   


class Skill(models.Model):
    name = models.CharField(max_length=12)
    slug = models.SlugField(max_length=12, unique=True)
    description = models.TextField(blank=True)
    icon_class = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class Project(models.Model):
    name = models.CharField(max_length=25)
    img = models.ImageField()
    text = models.TextField(max_length=470)
    skills = models.ManyToManyField(Skill, blank=True)
    deploy = models.URLField(max_length=300)
    repository = models.URLField(max_length=300)
