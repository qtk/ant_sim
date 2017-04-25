import sys
import random
from time import sleep
import pygame

pygame.init()

# directions
dirs = {"NORTH": (0, -1),
        "EAST": (1, 0),
        "SOUTH": (0, 1),
        "WEST": (-1, 0)}


class MovingPixel:
    """ A moving pixel class. """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hdir = 0
        self.vdir = 0

    def choose_direction(self, dir=(0, 0), free=False):
        """ Changes the pixels direction. """
        if not free:
            self.hdir, self.vdir = dir
        else:
            self.hdir, self.vdir = dirs[random.choice(list(dirs))]

    def move(self):
        """ Moves the pixel. """
        self.x += self.hdir
        self.y += self.vdir

# window dimensions
size = width, height = (1000, 500)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True

# create a moving pixel
pixel = MovingPixel(width//2, height//2)

# set background color
screen.fill((255, 255, 255))

while running:
    pixel.move()

    if pixel.x < 0 or pixel.x >= width or pixel.y < 0 or pixel.y >= height:
        print("Chrash!")
        running = False

    screen.set_at((pixel.x, pixel.y), (0, 0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        pixel.choose_direction(dirs["NORTH"])
    elif pressed[pygame.K_DOWN]:
        pixel.choose_direction(dirs["SOUTH"])
    elif pressed[pygame.K_LEFT]:
        pixel.choose_direction(dirs["WEST"])
    elif pressed[pygame.K_RIGHT]:
        pixel.choose_direction(dirs["EAST"])
    else:
        pixel.choose_direction(free=True)

    pygame.display.flip()
    clock.tick(60)
