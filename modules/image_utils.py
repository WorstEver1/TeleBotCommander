from PIL import Image
import os
from .exceptions import NotCorrectImage

def image_is_correct(image_path) -> bool:
    """
    Checks if the image is valid and returns the result. If an error occurs, raises an exception.
    """

    try:
        return image_larger_than_normal(image_path) and image_weight_larger_than_normal(image_path)
    except:
        raise NotCorrectImage(f'Bad image {image_path}!')
    
def image_larger_than_normal(image_path) -> bool:
    """
    Checks if the total of the image's dimensions exceeds 10000 pixels. 
    Returns False if it does, True otherwise.
    """


    with Image.open(image_path) as img:
            width, height = img.size

            if height + width > 10000:
                return False
            return True

def image_weight_larger_than_normal(image_path) -> bool:
    """
    Checks if the image's size exceeds 10 MB. 
    Returns False if it does, True otherwise.
    """
    size_in_MB = os.path.getsize(image_path) / (1024 * 1024)
    
    if size_in_MB > 10:
        return False
    return True