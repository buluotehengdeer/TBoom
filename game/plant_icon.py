import pygame
from pygame.sprite import Sprite
from cnf.settings import Settings

class Plant_Icon(Sprite):
    def __init__(self, game_settings, icon, slot):
        super(Plant_Icon, self).__init__()
        self.image = pygame.image.load(Settings.BASE_DIR + 'game/images/' + icon)
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.left = 300 + (110 * slot)
        self.rect.top = 30
        self.slot = slot
