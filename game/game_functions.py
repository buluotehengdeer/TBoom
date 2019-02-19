import sys
import pygame
from game.peashooter import Peashooter
from game.gatling import Gatling
from game.bullet import Bullet
import time
from game.sunflower import Sunflower


def check_events(screen, game_settings, squares, plants, bullets, icons):
    '''
        事件监视
    '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if game_settings.game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for square in squares:
                    # 冲突检查,同点进行冲突检查，也就是判断是否点击
                    if square.rect.collidepoint(mouse_x, mouse_y):
                        if(game_settings.chosen_plant == 1):
                            if game_settings.total_sun - Peashooter.sun_cost >= 0:
                                plants.add(Peashooter(screen, square))
                                game_settings.total_sun -= Peashooter.sun_cost
                        elif(game_settings.chosen_plant == 2):
                            if game_settings.total_sun - Gatling.sun_cost >= 0:
                                plants.add(Gatling(screen, square))
                                game_settings.total_sun -= Gatling.sun_cost
                        elif(game_settings.chosen_plant == 3):
                            if game_settings.total_sun - Sunflower.sun_cost >= 0:
                                plants.add(Sunflower(screen, square))
                                game_settings.total_sun -= Sunflower.sun_cost
                for icon in icons:
                    if icon.rect.collidepoint(mouse_x, mouse_y):
                        game_settings.chosen_plant = icon.slot

            elif event.type == pygame.MOUSEMOTION:
                for square in squares:
                    if square.rect.collidepoint(event.pos):
                        game_settings.highlighted_square = square


def update_screen(screen, game_settings, background, zombies, squares, plants, bullets, tick, icons):
    '''
        更新(画)游戏图形
    '''
    screen.blit(background.image, background.rect)
    for icon in icons:
        screen.blit(icon.image, icon.rect)

    if game_settings.highlighted_square != 0:
        pygame.draw.rect(screen, (255, 215, 0), (game_settings.highlighted_square.rect.left, game_settings.highlighted_square.rect.top,
                                                 game_settings.squares['square_width'], game_settings.squares['square_height']), 5)

    # 画僵尸
    for zombie in zombies.sprites():
        if game_settings.game_active:
            zombie.update_me()
        zombie.draw_me()
        if zombie.rect.left <= zombie.screen_rect.left:
            game_settings.game_active = False
        zombie.moving = True

    # 画植物
    for plant in plants:
        plant.draw_me()
        should_shoot = time.time() - plant.last_shot > plant.shoot_speed
        can_shoot = plant.can_shoot
        in_my_row = game_settings.zombie_in_row[plant.yard_row] > 0
        if should_shoot and in_my_row and can_shoot:
            bullets.add(Bullet(screen, plant))
            plant.last_shot = time.time()
        can_make_sun = plant.can_make_sun
        should_make_sun = time.time() - plant.last_sun > plant.sun_speed
        if can_make_sun and should_make_sun:
            plant.make_sun(game_settings)
            plant.last_sun = time.time()

    for bullet in bullets.sprites():
        bullet.update_me()
        bullet.draw_me()

    score_font = pygame.font.SysFont("monospace", 36)
    # render a font takes 3 params:
    # 1. What text.
    # 2. I cant remember
    # 3. Color
    score_render = score_font.render(
        "Killed: " + str(game_settings.zombies_killed) + "!", 1, (255, 215, 0));
    screen.blit(score_render, (100, 20))

    sun_render = score_font.render(
        "Sun: " + str(game_settings.total_sun) + "!", 1, (255, 215, 0));
    screen.blit(sun_render, (100, 40))
