'''
Rainbower.

Desc:
generates a rainbow

Tools:
Pygame
'''
from random import randint
import pygame


class Bit:
    def __init__(self, x, y, width, height, r, g, b):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.r = r
        self.g = g
        self.b = b

        self.color = pygame.Color(self.r, self.g, self.b)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


def setup():
    pygame.init()

    WINDOW = pygame.display.set_mode((800, 200))

    bits = []
    maxBits = 20

    # fill array with bits
    while len(bits) < maxBits:
        width = WINDOW.get_width() / maxBits
        height = WINDOW.get_height()
        x = len(bits) * width
        y = 0
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)

        bit = Bit(x, y, width, height, r, g, b)
        bits.append(bit)

    # draw colors
    for bit in bits:
        pygame.draw.rect(WINDOW, bit.color, bit.rect)

        print('\nBit index ' + str(bits.index(bit)))
        print('    x: ' + str(bit.x))
        print('    y: ' + str(bit.y))
        print('    width: ' + str(bit.width))
        print('    height: ' + str(bit.height))
        print('    rgb: ' + str(bit.r), str(bit.g), str(bit.b))

    print('\nTotal n of bits = ' + str(len(bits)))


def update():
    '''update'''
    run = True
    while run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

def draw():
    '''draw'''
