import pygame
from pygame.sprite import Sprite
from cnf.settings import Settings


class Rank(Sprite):
    def __init__(self, icon, slot):
        super(Rank, self).__init__()
        self.image = icon
        self.image = pygame.transform.scale(self.image, (140, 80))
        self.rect = self.image.get_rect()
        self.rect.left = 30
        self.rect.top = 20 + (50 * slot)
        self.slot = slot
