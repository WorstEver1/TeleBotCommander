from PIL import Image
import os

def image_is_correct(image_path) -> bool:
    try:
        return image_larger_than_normal(image_path) and image_weight_larger_than_normal(image_path)
    except:
        raise Exception(f'Bad image {image_path}!')
    
def image_larger_than_normal(image_path) -> bool:

    with Image.open(image_path) as img:
            width, height = img.size

            if height + width > 10000:
                return False
            return True

def image_weight_larger_than_normal(image_path) -> bool:
    size_in_MB = os.path.getsize(image_path) / (1024 * 1024)
    
    if size_in_MB > 10:
        return False
    return True