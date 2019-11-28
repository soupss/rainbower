'''
Rainbower.

Desc:
generates N colors and sorts by hue, resulting in a random rainbow.

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

    def draw(self, surface):
        '''Draw bit to the specified surface'''
        pygame.draw.rect(surface, self.color, self.rect)

    def log(self, index):
        '''Log information about bit'''
        print('\nBit n' + str(index + 1))
        print('rgb: ' + str(self.color.r), str(self.color.g), str(self.color.b))
        print('pos: ' + str(self.rect.x))
        print('hue: ' + str(self.color.hsva[0]))


def hue(elem):
    '''Get hue of element with color object'''
    return elem.color.hsva[0]


def setup():
    '''Setup program variables'''
    pygame.init()

    window = pygame.display.set_mode((1000, 200))

    bits = []
    max_bits = 25 # window.get_width() % max_bit equal to 0 for best performance

    # fill array with bits
    while len(bits) < max_bits:
        width = window.get_width() / max_bits
        height = window.get_height()
        x = 0
        y = 0
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)

        color = pygame.Color(r, g, b)
        rect = pygame.Rect(x, y, width, height)

        bit = Bit(color, rect)
        bits.append(bit)

    # sort bits in array
    bits.sort(key=hue)
    for index, bit in enumerate(bits):
        # sort bits visually
        bit.rect.x = index * bit.rect.width

        #draw bits
        bit.draw(window)
        bit.log(index)


def update():
    '''Update program variables'''
    run = True
    while run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
