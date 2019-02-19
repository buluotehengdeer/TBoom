import pygame
from pygame.sprite import Sprite
from cnf.settings import Settings

'''
    子弹精灵
'''
class Bullet(Sprite):
    def __init__(self, screen, plant):
        super(Bullet, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load(
            Settings.BASE_DIR + 'game/images/Giant_Pea2.png')
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()

        self.rect.centerx = plant.rect.centerx
        self.rect.top = plant.rect.top + 20
        self.yard_row = plant.yard_row

        self.x = self.rect.x
        self.y = self.rect.y

    def draw_me(self):
        '''
            将精灵的图片画到屏幕上
        '''
        self.screen.blit(self.image, self.rect)

    def update_me(self):
        self.x += 15
        self.rect.x = self.x
