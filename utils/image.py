from PIL import Image
import io
from django.core.files.base import ContentFile

def resize_image(image_file, new_size=400, optimize=True, quality=60):
    # Abre a imagem
    image = Image.open(image_file)
    
    # Define o formato da imagem
    format = image.format or 'PNG'  # Usa PNG como padrão se o formato não estiver definido
    
    # Redimensiona a imagem para um quadrado
    image = image.resize((new_size, new_size), Image.LANCZOS)
    
    # Salva a nova imagem em um buffer
    image_io = io.BytesIO()
    image.save(image_io, format=format, optimize=optimize, quality=quality)
    
    # Cria um ContentFile para o Django
    return ContentFile(image_io.getvalue(), image_file.name)

