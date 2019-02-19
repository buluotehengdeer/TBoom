import pygame
from pygame.locals import *
from game.settings import Settings
from game.background import Background
import game.game_functions as gf
from pygame.sprite import Group, groupcollide
from game.zombie import Zombie, Zombie1, Zombie3, Zombie4, Zombie5
from game.square import Square
from game.plant_icon import Plant_Icon
from game.button import Button
import time
from random import randint
from cnf.settings import Settings as st
import sys
from db import db
from game.rank import Rank

Login_username = ''

pygame.init()
game_settings = Settings()
screen = pygame.display.set_mode(game_settings.screen_size)
pygame.display.set_caption("DC PvZ clone")
background = Background(game_settings)
peashooter_icon = Plant_Icon(game_settings, 'peashooter-icon.png', 1)
gatling_icon = Plant_Icon(game_settings, 'gatling-icon.png', 2)
sunflower_icon = Plant_Icon(game_settings, 'sunflower.png', 3)
icons = [peashooter_icon, gatling_icon, sunflower_icon]

# All our groups
zombies = Group()
plants = Group()
squares = Group()
bullets = Group()

game_level = game_settings.level


def textToImage(font, text, color=(255, 0, 0)):
    '''
        将文字转成图片
    '''
    imgText = font.render(text, True, color)
    return imgText


def print_text(screen, text1, text2, color=(255, 0, 0)):
    '''
        将文字输出到屏幕
    '''
    font = pygame.font.SysFont("monospace", 80)
    imgText = font.render(text1, True, color)
    imgText2 = font.render(text2, True, color)
    while True:
        screen.blit(imgText, (350, 230))
        screen.blit(imgText2, (200, 330))
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                global game_settings, zombies, plants, squares, bullets
                game_settings = Settings()
                game_settings.level = game_level
                zombies = Group()
                plants = Group()
                bullets = Group()
                run_game()
                return
        pygame.display.update()


def rank():
    '''
        排行榜界面
    '''
    global screen
    rank = db.getRank()
    rank = rank[0:11]
    font = pygame.font.SysFont("monospace", 80)
    rankContents = []
    for i in range(len(rank)):
        rankContents.append(Rank(textToImage(
            font, str(rank[i][0]) + "   " + str(rank[i][1])), i))
    background = pygame.image.load(
        st.BASE_DIR + "game/images/parmPage.jpeg").convert()
    while True:
        screen.blit(background, (0, 0))
        for rankContent in rankContents:
            screen.blit(rankContent.image, rankContent.rect)
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                getParm()
                return
        pygame.display.update()


def getParm():
    '''
        初始化并获得游戏的参数(游戏难度等)
    '''
    global screen
    global game_settings
    font = pygame.font.SysFont("monospace", 80)
    bt_start = Button(textToImage(font, "New Game"), 1)
    bt_level = Button(textToImage(font, "Level:"), 2)
    bt_level1 = Button(textToImage(font, "1"), 3)
    bt_level2 = Button(textToImage(font, "2"), 4)
    bt_level3 = Button(textToImage(font, "3"), 5)
    bt_rank = Button(textToImage(font, "Rank"), 6)
    bt_levels = [bt_level1, bt_level2, bt_level3]
    background = pygame.image.load(
        st.BASE_DIR + "game/images/parmPage.jpeg").convert()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if bt_start.rect.collidepoint(mouse_x, mouse_y):
                    return
                elif bt_rank.rect.collidepoint(mouse_x, mouse_y):
                    rank()
                for level in bt_levels:
                    if level.rect.collidepoint(mouse_x, mouse_y):
                        game_settings.level = level.slot - 2
                        return

        screen.blit(background, (0, 0))
        screen.blit(bt_start.image, bt_start.rect)
        screen.blit(bt_level.image, bt_level.rect)
        screen.blit(bt_level1.image, bt_level1.rect)
        screen.blit(bt_level2.image, bt_level2.rect)
        screen.blit(bt_level3.image, bt_level3.rect)
        screen.blit(bt_rank.image, bt_rank.rect)
        pygame.display.update()


for i in range(0, 5):
    for j in range(0, 9):
        squares.add(Square(screen, game_settings, i, j))


def run_game():
    '''
        开始游戏
    '''
    global Login_username
    tick = 0
    zombieList = [Zombie, Zombie1, Zombie3, Zombie4, Zombie5]
    while 1:
        # 开始监听事件
        gf.check_events(screen, game_settings, squares, plants, bullets, icons)
        # 如果游戏没结束
        if game_settings.game_active:
            tick += 1
            # 如果满足添加僵尸的条件就添加僵尸
            if tick % game_settings.addZombieTime == 0 and game_settings.total_zombie:
                if game_settings.level == 1:
                    # 在0-1号僵尸中随机添加一个
                    zombie = zombieList[randint(0, 1)]
                    zombies.add(zombie(screen, game_settings))
                elif game_settings.level == 2:
                    # 在0-3号僵尸中随机添加一个
                    zombie = zombieList[randint(0, 3)]
                    zombies.add(zombie(screen, game_settings))
                elif game_settings.level == 3:
                    zombie = zombieList[randint(0, 4)]
                    zombies.add(zombie(screen, game_settings))
                game_settings.total_zombie -= 1

            # 僵尸同子弹的碰撞检测
            zombies_hit = groupcollide(zombies, bullets, False, False)
            for zombie in zombies_hit:
                if zombie.yard_row == zombies_hit[zombie][0].yard_row:
                    bullets.remove(zombies_hit[zombie][0])
                    zombie.hit(1)
                    if(zombie.health <= 0):
                        zombies.remove(zombie)
                        game_settings.zombie_in_row[zombie.yard_row] -= 1
                        game_settings.zombies_killed += 1
            zombies_eating = groupcollide(zombies, plants, False, False)
            for zombie in zombies_eating:
                damaged_plant = zombies_eating[zombie][0]
                if zombie.yard_row == damaged_plant.yard_row:
                    zombie.moving = False
                    if time.time() - zombie.started_eating > zombie.damage_time:
                        zombie.zombie_chomp(damaged_plant)
                        zombie.started_eating = time.time()
                        if damaged_plant.health <= 0:
                            plants.remove(damaged_plant)
                            zombie.moving = True
        if game_settings.game_active and game_settings.total_zombie == 0:
            global game_level
            game_settings.level += 1
            game_level += 1
            # 更新分数
            db.updateScore(Login_username, game_settings.level *
                           game_settings.zombies_killed)
            print_text(screen, "WIN!", "Next Level " +
                       str(game_settings.level))
            return

        elif game_settings.game_active is False:
            db.updateScore(Login_username, game_settings.level *
                           game_settings.zombies_killed)
            print_text(screen, "Game Over!", '')
            return

        gf.update_screen(screen, game_settings, background,
                         zombies, squares, plants, bullets, tick, icons)
        pygame.display.flip()


def run(username):
    global Login_username
    Login_username = username
    getParm()
    run_game()
