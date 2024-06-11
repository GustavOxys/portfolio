from pathlib import Path
from PIL import Image


def resize_image_to_square(image_path, new_size=800, optimize=True, quality=60, output_path=None):
    
    image_path = Path(image_path)
    image_pillow = Image.open(image_path)

    # Redimensiona a imagem para um quadrado
    new_image = image_pillow.resize((new_size, new_size), Image.LANCZOS)

    # Determina o caminho para salvar a nova imagem
    if output_path is None:
        output_path = image_path.parent / (image_path.stem + f"_resized{new_size}.png")
    else:
        output_path = Path(output_path)

    # Salva a nova imagem
    new_image.save(
        output_path,
        optimize=optimize,
        quality=quality,
    )

    return new_image




def resize_and_crop_image(image_path, new_size=(800, 800), optimize=True, quality=60, output_path=None):
    
    image_path = Path(image_path)
    image_pillow = Image.open(image_path)

    
    image_pillow.thumbnail(new_size)

    
    width, height = image_pillow.size
    left = (width - new_size[0]) / 2
    top = (height - new_size[1]) / 2
    right = (width + new_size[0]) / 2
    bottom = (height + new_size[1]) / 2

    
    cropped_image = image_pillow.crop((left, top, right, bottom))

    
    if output_path is None:
        output_path = image_path.parent / (image_path.stem + "_cropped.jpg")
    else:
        output_path = Path(output_path)

    
    cropped_image.save(
        output_path,
        optimize=optimize,
        quality=quality,
    )

    return cropped_image

imagem = 'base_static/global/blog-front.png'
resize_image_to_square(imagem, new_size=400)
resize_and_crop_image(imagem)