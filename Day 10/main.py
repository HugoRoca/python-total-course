import pygame
import random
import math
from pygame import mixer

# Init pygame
pygame.init()

# Init screen
screen = pygame.display.set_mode((800, 600))

# Custom title and icon
pygame.display.set_caption('Invasion Game')
icon = pygame.image.load('ovni.png')
pygame.display.set_icon(icon)
background = pygame.image.load('Fondo.jpg')
font_end_text = pygame.font.Font('freesansbold.ttf', 40)

# music
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.2)
mixer.music.play(-1)

# Player
img_player = pygame.image.load('cohete.png')
player_x = 368
player_y = 500
player_change = 0

img_enemy = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
enemy_total = 8

for i in range(enemy_total):
    img_enemy.append(pygame.image.load('enemigo.png'))
    enemy_x.append(random.randint(0, 736))
    enemy_y.append(random.randint(50, 200))
    enemy_x_change.append(0.7)
    enemy_y_change.append(50)

img_bullet = pygame.image.load('bala.png')
bullet_x = 0
bullet_y = 500
bullet_y_change = 3
bullet_visible = False

# Points
points = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10


def show_point(x, y):
    text = font.render(f'Points: {points}', True, (255, 255, 255))
    screen.blit(text, (x, y))


def build_player(x, y):
    screen.blit(img_player, (x, y))


def build_enemy(x, y, i):
    screen.blit(img_enemy[i], (x, y))


def shot_bullet(x, y):
    global bullet_visible
    bullet_visible = True
    screen.blit(img_bullet, (x + 16, y + 10))


def detect_crash(x_1, y_1, x_2, y_2):
    distance = math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2))
    return distance < 27


def end_text():
    my_end_font = font_end_text.render('END GAME', True, (255, 255, 255))
    screen.blit(my_end_font, (60, 200))


# Loop game
execute = True
while execute:
    # background
    screen.blit(background, (0, 0))

    # events loop
    for event in pygame.event.get():
        # for close game
        if event.type == pygame.QUIT:
            execute = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change = -1.5
            if event.key == pygame.K_RIGHT:
                player_change = 1.5
            if event.key == pygame.K_SPACE:
                if not bullet_visible:
                    mixer.Sound('disparo.mp3').play()
                    bullet_x = player_x
                    shot_bullet(bullet_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_change = 0

    # change position
    player_x += player_change

    # valid position
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # valid position
    for i in range(enemy_total):
        # End game
        if enemy_y[i] > 450:
            for k in range(enemy_total):
                enemy_y[k] = 1000

            end_text()
            break

        enemy_x[i] += enemy_x_change[i]

        if enemy_x[i] <= 0:
            enemy_x_change[i] = 1
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] >= 736:
            enemy_x_change[i] = -1
            enemy_y[i] += enemy_y_change[i]

        crash = detect_crash(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if crash:
            mixer.Sound('Golpe.mp3').play()
            bullet_y = 500
            bullet_visible = False
            points += 1
            enemy_x[i] = random.randint(0, 736)
            enemy_y[i] = random.randint(50, 200)

        build_enemy(enemy_x[i], enemy_y[i], i)

    if bullet_y <= -64:
        bullet_y = 500
        bullet_visible = False
    if bullet_visible:
        shot_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    build_player(player_x, player_y)
    show_point(text_x, text_y)
    pygame.display.update()


