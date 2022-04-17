import sys

import numba
import numpy
import pygame as pg

pg.init()

WHITE = [255, 255, 255]
BLACK = [0, 0, 0]

WINDOW_SHAPE = [1000, 800]

screen = pg.display.set_mode(WINDOW_SHAPE)


while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    screen.fill(BLACK)

    pg.display.update()
