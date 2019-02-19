import pygame
from pygame.sprite import Sprite


class Plant(Sprite):
    def __init__(self):
        super(Plant, self).__init__()

        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load(self.image_file)
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.left = self.square.rect.left
        self.rect.top = self.square.rect.top
        self.yard_row = self.square.row_number
        self.last_shot = 0
        self.last_sun = 0

    def draw_me(self):
        self.screen.blit(self.image, self.rect)
