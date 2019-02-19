import pygame


class Settings():
    def __init__(self):
        display_info = pygame.display.Info()
        self.screen_size = (800, 500)
        self.bg_color = (255, 255, 255)
        self.level = 1
        self.zombie_speed = 0.5 * self.level
        self.addZombieTime = 800 // self.level
        self.zombie_health = 5 * self.level
        self.game_active = True
        self.chosen_plant = 1
        self.zombies_killed = 0
        self.total_sun = 100 * self.level
        self.total_zombie = 10
        # square stuff
        self.squares = {
            "start_left": 200,
            "start_top": 130,
            "square_width": 60,
            "square_height": 60,
            "rows": [
                130,
                190,
                250,
                310,
                370
            ]
        };
        self.highlighted_square = 0
        self.zombie_in_row = [
            0,
            0,
            0,
            0,
            0
        ]
