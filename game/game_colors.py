import random
import pygame


class GameColors:
    @staticmethod
    def get_random_color() -> (int, int, int):
        color_values = list(pygame.colordict.THECOLORS.values())
        r, g, b, _ = color_values[random.randrange(len(color_values)-1)]
        return r, g, b
