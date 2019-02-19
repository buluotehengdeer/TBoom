import pygame
from pygame.sprite import Sprite
from random import randint
from cnf.settings import Settings


class Zombie(Sprite):
    def __init__(self, screen, game_settings):
        super(Zombie, self).__init__()
        self.speed = game_settings.zombie_speed
        self.health = game_settings.zombie_health
        self.image = pygame.image.load(
            Settings.BASE_DIR + 'game/images/Crazyzombie.gif')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.yard_row = randint(0, 4)
        self.rect.centery = game_settings.squares["rows"][self.yard_row]
        self.rect.right = self.screen_rect.right
        game_settings.zombie_in_row[self.yard_row] += 1

        self.x = float(self.rect.x)
        self.moving = True
        self.started_eating = 0
        self.damage_time = 2

    def update_me(self):
        if self.moving:
            self.x -= self.speed * 1
            self.rect.x = self.x

    def draw_me(self):
        self.screen.blit(self.image, self.rect)

    def hit(self, damage):
        self.health -= damage

    def zombie_chomp(self, plant):
        plant.health -= 1


class Zombie1(Sprite):
    def __init__(self, screen, game_settings):
        super(Zombie1, self).__init__()
        self.speed = game_settings.zombie_speed
        self.health = game_settings.zombie_health
        self.image = pygame.image.load(
            Settings.BASE_DIR + 'game/images/Crazyzombie1.gif')
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.yard_row = randint(0, 4)
        self.rect.centery = game_settings.squares["rows"][self.yard_row]
        self.rect.right = self.screen_rect.right
        game_settings.zombie_in_row[self.yard_row] += 1

        self.x = float(self.rect.x)
        self.moving = True
        self.started_eating = 0
        self.damage_time = 2

    def update_me(self):
        if self.moving:
            self.x -= self.speed * 1
            self.rect.x = self.x

    def draw_me(self):
        self.screen.blit(self.image, self.rect)

    def hit(self, damage):
        self.health -= damage

    def zombie_chomp(self, plant):
        plant.health -= 1


class Zombie3(Sprite):
    def __init__(self, screen, game_settings):
        super(Zombie3, self).__init__()
        self.speed = game_settings.zombie_speed
        self.health = game_settings.zombie_health
        self.image = pygame.image.load(
            Settings.BASE_DIR + 'game/images/Crazyzombie3.gif')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.yard_row = randint(0, 4)
        self.rect.centery = game_settings.squares["rows"][self.yard_row]
        self.rect.right = self.screen_rect.right
        game_settings.zombie_in_row[self.yard_row] += 1

        self.x = float(self.rect.x)
        self.moving = True
        self.started_eating = 0
        self.damage_time = 2

    def update_me(self):
        if self.moving:
            self.x -= self.speed * 1
            self.rect.x = self.x

    def draw_me(self):
        self.screen.blit(self.image, self.rect)

    def hit(self, damage):
        self.health -= damage

    def zombie_chomp(self, plant):
        plant.health -= 1


class Zombie4(Sprite):
    def __init__(self, screen, game_settings):
        super(Zombie4, self).__init__()
        self.speed = game_settings.zombie_speed
        self.health = game_settings.zombie_health
        self.image = pygame.image.load(
            Settings.BASE_DIR + 'game/images/Crazyzombie4.gif')
        self.image = pygame.transform.scale(self.image, (110, 110))
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.yard_row = randint(0, 4)
        self.rect.centery = game_settings.squares["rows"][self.yard_row]
        self.rect.right = self.screen_rect.right
        game_settings.zombie_in_row[self.yard_row] += 1

        self.x = float(self.rect.x)
        self.moving = True
        self.started_eating = 0
        self.damage_time = 2

    def update_me(self):
        if self.moving:
            self.x -= self.speed * 1
            self.rect.x = self.x

    def draw_me(self):
        self.screen.blit(self.image, self.rect)

    def hit(self, damage):
        self.health -= damage

    def zombie_chomp(self, plant):
        plant.health -= 1


class Zombie5(Sprite):
    def __init__(self, screen, game_settings):
        super(Zombie5, self).__init__()
        self.speed = game_settings.zombie_speed
        self.health = game_settings.zombie_health
        self.image = pygame.image.load(
            Settings.BASE_DIR + 'game/images/Crazyzombie5.gif')
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.yard_row = randint(0, 4)
        self.rect.centery = game_settings.squares["rows"][self.yard_row]
        self.rect.right = self.screen_rect.right
        game_settings.zombie_in_row[self.yard_row] += 1

        self.x = float(self.rect.x)
        self.moving = True
        self.started_eating = 0
        self.damage_time = 2

    def update_me(self):
        if self.moving:
            self.x -= self.speed * 1
            self.rect.x = self.x

    def draw_me(self):
        self.screen.blit(self.image, self.rect)

    def hit(self, damage):
        self.health -= damage

    def zombie_chomp(self, plant):
        plant.health -= 1
