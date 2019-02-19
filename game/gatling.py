import pygame
from pygame.sprite import Sprite
from game.plant import Plant
from cnf.settings import Settings


class Gatling(Plant):
    sun_cost = 150

    def __init__(self, screen, square):
        self.shoot_speed = 1
        self.health = 6
        self.image_file = Settings.BASE_DIR + 'game/images/Gatling_Pea_Fixed.png'
        self.screen = screen
        self.square = square
        self.name = "gatling"
        self.can_shoot = True
        self.can_make_sun = False
        self.sun_speed = 0
        super(Gatling, self).__init__()
