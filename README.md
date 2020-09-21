# SPACE INVADERS

Creating a game of space invaders using pygame. The idea is inspired by the following youtube video from Free code camp
[FreeCodeCamp](https://www.youtube.com/watch?v=FfWpgLFMI7w&t=1780s&ab_channel=freeCodeCamp.org)

The aim of this project is to get used to github as well as share my learnings about pygame.

## Learnings

1. **The Pygame community provides us with a screen. Everything we do is on that screen.**

2. **If we just initialize the screen it will vanish after a moment. So to keep the screen running we need a while loop and it will run untill we click close button**

3. **Every event on that screen is caputured by pygame including mouse hovering to keystroke. Used this advantage to move the spaceship from one position to another**

4. **ALways in while loop initialize the screen first, change its color and e=more before using any icons or any other thing. Because if we add icon first and then change the screen we will not be able to see the icons as screen will be on icon. We want icons on screen.**

5. **If we load a background image the motion of spaceship and invaders will become slow. So after adding the bg-image increase the speed.**


## Details
Used pygame to create a space invader game. The aim of the game is to kill all the space invaders that are trying to attack your planet. If  a invader is able to bypass yoyur spaceship somehow you will loose the game. The more you kill the more points you earn. 
Used python for coding. 
