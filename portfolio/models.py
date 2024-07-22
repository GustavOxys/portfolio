from django.db import models
from django.utils.text import slugify
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

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
    image = models.ImageField(upload_to='base_static/global/media/')
    text = models.TextField(max_length=470)
    skills = models.ManyToManyField(Skill, blank=True)
    deploy = models.URLField(max_length=300, blank=True)
    repository = models.URLField(max_length=300, blank=True)

    def save(self, *args, **kwargs):
        if self.image and hasattr(self.image, 'file'):
            # Redimensiona a imagem
            image_file = self.image.file
            image_pillow = Image.open(image_file)
            new_image = self.resize_image(image_pillow, new_size=400)

            # Salva a imagem redimensionada
            image_io = BytesIO()
            new_image.save(image_io, format='PNG', quality=60)
            image_file = ContentFile(image_io.getvalue(), name=self.image.name)
            
            self.image.save(self.image.name, image_file, save=False)

        super().save(*args, **kwargs)

    def resize_image(self, image_pillow, new_size=400):
        # Redimensiona a imagem para um quadrado
        return image_pillow.resize((new_size, new_size), Image.LANCZOS)