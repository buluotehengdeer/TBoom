import pygame
from pygame.sprite import Sprite
from game.plant import Plant
from cnf.settings import Settings


class Peashooter(Plant):
    sun_cost = 50

    def __init__(self, screen, square):
        self.shoot_speed = 3
        self.image_file = Settings.BASE_DIR + 'game/images/peashooter.png'
        self.screen = screen
        self.square = square
        self.name = "peashooter"
        self.health = 5
        self.can_shoot = True
        self.can_make_sun = False
        self.sun_speed = 0

        super(Peashooter, self).__init__()
