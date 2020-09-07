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


# we can observe here that the screen disappears quickly. To change that
# one way is

# while True:
#     pass

# but this will hang the window as it is neverending loop

# so we will close the windo when someone is clicking on x button
# for that we will use the following code


is_running = 1
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = 0

    # changing background color using rgb values and have to update to have change in effect
    screen.fill((185, 198, 221))
    pygame.display.update()
