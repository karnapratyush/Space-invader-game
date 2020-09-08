# importing pygame
import pygame


# initializing the pygame
pygame.init()


# creating a screen

screen = pygame.display.set_mode((800, 600))


# changing the Title and icon of the window
pygame.display.set_caption(" Space Invaders")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

# setting the spaceship and adding it at certain fixed position on screen
spaceship_icon = pygame.image.load("space-invaders.png")
spaceship_static_x = 370
spaceship_static_y = 500
playerX_change = 0


def player(x, y):
    # drawing a image on screen is written below

    screen.blit(spaceship_icon, (x, y))


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

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            is_running = 0

        # checking whether the keystroke(key pressed ) is right or left arrow key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        #         playerX_change = 0

    spaceship_static_x += playerX_change
    player(spaceship_static_x, spaceship_static_y)
    pygame.display.update()
