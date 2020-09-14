# importing pygame
import pygame

# importing random so that enemy can appear from anywhere
import random


# initializing the pygame
pygame.init()


# creating a screen

screen = pygame.display.set_mode((800, 600))


# changing the Title and icon of the window
pygame.display.set_caption(" Space Invaders")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

# adding bg-image
bg = pygame.image.load("background_image.png")

# setting the spaceship and adding it at certain fixed position on screen
spaceship_icon = pygame.image.load("space-invaders.png")
spaceship_static_x = 370
spaceship_static_y = 500
playerX_change = 0


# adding ememies
enemy_icon = pygame.image.load("alien.png")
enemy_x = random.randint(0, 736)
enemy_y = 0
enemy_pos_diff_X = 1
enemy_pos_diff_Y = 0


# adding bullet
bullet_icon = pygame.image.load("bullet32px.png")
fire = 0
bullet_Y = spaceship_static_y
bullet_X = spaceship_static_x


def player(x, y):
    # drawing a image on screen is written below

    screen.blit(spaceship_icon, (x, y))


# defing enemy
def enemy(x, y):

    screen.blit(enemy_icon, (x, y))


# def bullet motion
def bullet(x, y):
    global fire
    fire = 1
    screen.blit(bullet_icon, (x + 16, y + 10))
    screen.blit(bullet_icon, (x, y + 10))
    screen.blit(bullet_icon, (x + 30, y + 10))


# checking if collision is happening
def collision(a_x, a_y, b_x, b_y):
    if (
        abs(b_y - a_y) < 96
        and abs((a_x + 64) - (b_x)) < 96
        and abs(b_x + 32 - a_x) < 96
    ):
        return 1
    return 0


score = 0


# we can observe here that the screen disappears quickly. To change that
# one way is

# while True:
#     pass

# but this will hang the window as it is neverending loop

# so we will close the windo when someone is clicking on x button


is_running = 1
while is_running:

    # changing background color using rgb values and have to update to have change in effect
    screen.fill((185, 198, 221))
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            is_running = 0

        # checking whether the keystroke(key pressed ) is right or left arrow key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                playerX_change = 3

            # setting up space bar to fire bullet
            if event.key == pygame.K_SPACE:
                # if not fired then only change the x-coordinate
                if fire == 0:
                    bullet_X = spaceship_static_x
                    bullet(bullet_X, bullet_Y)

        # when the keystroke is over return change to be zero so that static _x donnot change its positon
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    spaceship_static_x += playerX_change
    # setting up boundary
    if spaceship_static_x <= 0:
        spaceship_static_x = 0
    if spaceship_static_x >= 736:
        spaceship_static_x = 736

    # if enemy has touch the boundary then will come down
    if enemy_x >= 736:
        enemy_pos_diff_X = -1
        enemy_y += 10

    if enemy_x <= 0:
        enemy_pos_diff_X = 1
        enemy_y += 10

    # if a bullet was fired its y-coordinate should decrease
    if fire == 1:
        bullet_Y -= 3
        bullet(bullet_X, bullet_Y)
    # if bullet crossed the screen then fire should be set to zero so that next bullet can be fired
    if bullet_Y <= 0:
        fire = 0
        bullet_Y = spaceship_static_y

    enemy_x += enemy_pos_diff_X
    collided = collision(enemy_x, enemy_y, bullet_X, bullet_Y)
    if collided:
        bullet_Y = spaceship_static_y
        fire = 0
        score += 1
        print(score)
        enemy_x = random.randint(0, 736)
        enemy_y = 0

    enemy(enemy_x, enemy_y)

    player(spaceship_static_x, spaceship_static_y)

    pygame.display.update()
