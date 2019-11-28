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
        self.hue = self.color.hsva[0]
        self.sat = self.color.hsva[1] # saturation
        self.val = self.color.hsva[2] # value

    def draw(self, surface):
        '''Draw bit to the specified surface'''
        pygame.draw.rect(surface, self.color, self.rect)

    def log(self, index):
        '''Log information about bit'''
        print('\nBit ' + str(index + 1))
        print('rgb: ' + str(self.color.r), str(self.color.g), str(self.color.b))
        print('hsv: ' + str(int(self.hue)), str(int(self.sat)), str(int(self.val)))

def hue(bit):
    '''Get hue of bit class'''
    return bit.hue


def setup():
    '''Setup program variables'''
    print('''
    >>> Rainbower <<<
    ''')
    default_bits = 25

    config = enter_config = sat_config = val_config = bits_config = True
    while config:
        while enter_config:
            c = input('Config rainbow? Y/n: ').lower()
            if not c == 'y' and not c == 'n':
                print('Invalid input')
                continue
            elif c == 'y':
                default_sv = False
                print('default_sv set to ' + str(default_sv))
                enter_config = False
            elif c == 'n':
                default_sv = True
                max_bits = default_bits
                print('default_sv set to ' + str(default_sv))
                config = enter_config = False
        while sat_config and config:
            c = input('Enter min and max color saturation (values 0-100, separated by space): ')
            c = c.split(' ')
            if not len(c) == 2 and not c[0].isdigit() and not c[1].isdigit():
                print('Invalid input')
                continue
            c[0] = int(c[0])
            c[1] = int(c[1])
            if not 0 <= c[0] <= 100 and not 0 <= c[1] <= 100:
                print('Invalid input')
                continue
            min_sat = c[0]
            max_sat = c[1]

            print('min_sat set to ' + str(min_sat))
            print('max_sat set to ' + str(max_sat))
            sat_config = False
        while val_config and config:
            c = input('Enter min and max color value (values 0-100, separated by space): ')
            c = c.split(' ')
            # Check if c has two integers from 1-100
            if not len(c) == 2 and not c[0].isdigit() and not c[1].isdigit():
                print('Invalid input')
                continue
            c[0] = int(c[0])
            c[1] = int(c[1])
            if not 0 <= c[0] <= 100 and not 0 <= c[1] <= 100:
                print('Invalid input')
                continue
            min_val = c[0]
            max_val = c[1]

            print('min_val set to ' + str(min_val))
            print('max_val set to ' + str(max_val))
            val_config = False
        while bits_config and config:
            c = input('Enter amount of bits(N of colors)(values 1-1000, default ' + str(default_bits) + '): ')
            # check if c is digit from 1-1000
            if not c.isdigit() and not 1 <= int(c) <= 1000:
                print('Invalid input')
                continue
            if not 1000 % int(c) == 0:
                print(r'[!] 1000 % bits is NOT equal to 0')
                print('Rainbow width will not fill')
            max_bits = int(c)
            bits_config = False
        config = False

    pygame.init()
    window = pygame.display.set_mode((1000, 200))

    bits = []

    print('Generating rainbow... (progress ' + str(len(bits)) + '/' + str(max_bits) + ')')

    # fill array with bits
    while len(bits) < max_bits:
        width = window.get_width() / max_bits
        height = window.get_height()
        x = 0
        y = 0

        color_accept = False
        while not color_accept:
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)

            color = pygame.Color(r, g, b)
            rect = pygame.Rect(x, y, width, height)
            bit = Bit(color, rect)

            if not default_sv:
                if min_sat <= bit.sat <= max_sat and min_val <= bit.val <= max_val:
                    color_accept = True
                else:
                    continue
            else:
                bit.color.hsva = (bit.hue, 100, 100)
                color_accept = True
            bits.append(bit)
            print('Generating rainbow... (progress ' + str(len(bits)) + '/' + str(max_bits) + ')')
    print('Done!')

    # sort bits in array
    bits.sort(key=hue)
    for index, bit in enumerate(bits):
        # sort bits visually
        bit.rect.x = index * bit.rect.width

        # draw bits
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
