from os import sep
from pygame.image import load

_image_library = {}


def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image is None:
        canonicalized_path = path.replace('/', sep).replace('\\', sep)
        image = load(canonicalized_path)
        if path[-4:] == ".png":
            image.convert_alpha()
        _image_library[path] = image
    return image
