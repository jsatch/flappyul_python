import os
import pygame

def load_png(name):
    full_name = os.path.join('images', name)
    try:
        image = pygame.image.load(full_name)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except (pygame.error):
        print('No se puede cargar la imagen {}'.format(full_name))
        raise SystemExit("Error")

    return image, image.get_rect()
