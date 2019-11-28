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
    '''Bit of color'''
    def __init__(self, color, rect):
        self.color = color
        self.rect = rect


def setup():
    '''Setup program variables'''
    pygame.init()

    window = pygame.display.set_mode((800, 200))

    bits = []
    max_bits = 20

    # fill array with bits
    while len(bits) < max_bits:
        width = window.get_width() / max_bits
        height = window.get_height()
        x = len(bits) * width
        y = 0
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)

        color = pygame.Color(r, g, b)
        rect = pygame.Rect(x, y, width, height)

        bit = Bit(color, rect)
        bits.append(bit)

    # draw colors
    for bit in bits:
        pygame.draw.rect(window, bit.color, bit.rect)

        print('\nBit index ' + str(bits.index(bit)))
        print(' color: ' + str(bit.color))
        print(' rect: ' + str(bit.rect))

    print('\nTotal n of bits = ' + str(len(bits)))


def update():
    '''Update program variables'''
    run = True
    while run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
