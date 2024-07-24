from django.db import models
from django.utils.text import slugify
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

class About(models.Model):
    first_name = models.CharField(max_length=10)
    image = models.ImageField(upload_to='profile/%Y/%m/%d/')
    last_name = models.CharField(max_length=20)
    birth = models.DateField()
    about = models.TextField()
    age = models.IntegerField()

   


class Skill(models.Model):
    name = models.CharField(max_length=12)
    slug = models.SlugField(max_length=12, unique=True)
    description = models.TextField(blank=True)
    icon_class = models.CharField(max_length=100, blank=True)
    link = models.URLField(null=True, blank=True, max_length=400)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class Project(models.Model):
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to='projects/%Y/%m/%d/')
    image2 = models.ImageField(blank=True, null=True, upload_to='projects/%Y/%m/%d/')
    image3 = models.ImageField(blank=True, null=True, upload_to='projects/%Y/%m/%d/')
    resume = models.TextField(max_length=470)
    about_intro = models.TextField(blank=True, null=True)
    about_detail = models.TextField(blank=True, null=True)
    about_conclusion = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    deploy = models.URLField(max_length=300, blank=True)
    repository = models.URLField(max_length=300, blank=True)

    def save(self, *args, **kwargs):
        if self.image and hasattr(self.image, 'file'):
            self.image = self.process_image(self.image, new_size=400)
        if self.image2 and hasattr(self.image2, 'file'):
            self.image2 = self.process_image(self.image2, new_size=600)  
        if self.image3 and hasattr(self.image3, 'file'):
            self.image3 = self.process_image(self.image3, new_size=600)  

        super().save(*args, **kwargs)

    def process_image(self, image_field, new_size):
        image_file = image_field.file
        image_pillow = Image.open(image_file)
        new_image = self.resize_image(image_pillow, new_size=new_size)

        # Salva a imagem redimensionada
        image_io = BytesIO()
        new_image.save(image_io, format='PNG', quality=60)
        image_file = ContentFile(image_io.getvalue(), name=image_field.name)
        
        image_field.save(image_field.name, image_file, save=False)
        return image_field

    def resize_image(self, image_pillow, new_size):
        # Redimensiona a imagem para um quadrado
        return image_pillow.resize((new_size, new_size), Image.LANCZOS)
    
    def __str__(self):
        return self.name