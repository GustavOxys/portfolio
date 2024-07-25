from django.db import models
from django.utils.text import slugify
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
import hashlib

class About(models.Model):
    first_name = models.CharField(max_length=10)
    image = models.ImageField(upload_to='profile/%Y/%m/%d/')
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    about = models.TextField()


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
    image_hash = models.CharField(max_length=64, blank=True, editable=False)    
    resume = models.TextField(max_length=470)    
    skills = models.ManyToManyField(Skill, blank=True)
    deploy = models.URLField(max_length=300, blank=True)
    repository = models.URLField(max_length=300, blank=True)
    readme = models.URLField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        if self.pk:            
            old_instance = Project.objects.get(pk=self.pk)
            if old_instance.image and old_instance.image != self.image:                
                old_instance.image.delete(save=False)

        if self.image and hasattr(self.image, 'file'):            
            new_image_hash = self.calculate_image_hash(self.image)
            if self.image_hash != new_image_hash:
                self.image = self.process_image(self.image, new_size=400)
                self.image_hash = new_image_hash

        super().save(*args, **kwargs)

    def process_image(self, image_field, new_size):
        image_file = image_field.file
        image_pillow = Image.open(image_file)
        new_image = self.resize_image(image_pillow, new_size=new_size)
        
        image_io = BytesIO()
        new_image.save(image_io, format='PNG', quality=60)
        image_file = ContentFile(image_io.getvalue(), name=image_field.name)
        
        image_field.save(image_field.name, image_file, save=False)
        return image_field

    def resize_image(self, image_pillow, new_size):
        return image_pillow.resize((new_size, new_size), Image.LANCZOS)

    def calculate_image_hash(self, image_field):
        image_file = image_field.file
        image_file.seek(0)
        hash_md5 = hashlib.md5()
        for chunk in iter(lambda: image_file.read(4096), b""):
            hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    def __str__(self):
        return self.name