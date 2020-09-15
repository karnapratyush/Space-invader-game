# importing pygame
import pygame

from pygame import mixer

# importing random so that enemy can appear from anywhere
import random
impoort time


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


# adding number of ememies
enemy_icon = []
enemy_x = random.sample(range(0, 746), 6)
enemy_y = random.sample(range(0, 100), 6)
enemy_pos_diff_X = []
enemy_pos_diff_Y = []
number_of_aliens = 6
for i in range(number_of_aliens):
    enemy_icon.append(pygame.image.load("alien.png"))

    enemy_pos_diff_X.append(1)
    enemy_pos_diff_Y.append(0)


# adding bullet
bullet_icon = pygame.image.load("bullet32px.png")
fire = 0
bullet_Y = spaceship_static_y
bullet_X = spaceship_static_x


def player(x, y):
    # drawing a image on screen is written below

    screen.blit(spaceship_icon, (x, y))


# defing enemy
def enemy(x, y, i):

    screen.blit(enemy_icon[i], (x, y))


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
# adding score on scree
font = pygame.font.Font("freesansbold.ttf", 32)
text_x = 10
text_y = 10


def show_score():
    score_dis = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_dis, (text_x, text_y))


# adding songs
mixer.music.load("bg_sound.mp3")
mixer.music.play(-1)


# game over
over_font = pygame.font.Font("freesansbold.ttf", 64)
def game_over():
    game_over_dis = font.render("GAME OVER " , True, (255, 255, 255))
    screen.blit(game_over_dis, (200, 250))



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
                    # laser_song = mixer.Sound("laser.wav")
                    # laser_song.play()
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
    for i in range(number_of_aliens):
        if enemy_y[i]>200:
            game_over()
            for j in range(6):
                enemy_x[j]=800
            time.sleep(3)
            is_running=0
            break


            break
        if enemy_x[i] >= 736:
            enemy_pos_diff_X[i] = -1
            enemy_y[i] += 10

        elif enemy_x[i] <= 0:
            enemy_pos_diff_X[i] = 1
            enemy_y[i] += 10

        enemy_x[i] += enemy_pos_diff_X[i]
        enemy(enemy_x[i], enemy_y[i], i)
        collided = collision(enemy_x[i], enemy_y[i], bullet_X, bullet_Y)
        if collided:
            collision_song = mixer.Sound("explosion.wav")
            collision_song.play()

            bullet_Y = spaceship_static_y
            fire = 0
            score += 1
            print(score)
            enemy_x[i] = random.randint(0, 746)
            enemy_y[i] = random.randint(0, 100)

    # if a bullet was fired its y-coordinate should decrease
    if fire == 1:
        bullet_Y -= 3
        bullet(bullet_X, bullet_Y)
    # if bullet crossed the screen then fire should be set to zero so that next bullet can be fired
    if bullet_Y <= 0:
        fire = 0
        bullet_Y = spaceship_static_y

    player(spaceship_static_x, spaceship_static_y)
    show_score()
    pygame.display.update()
