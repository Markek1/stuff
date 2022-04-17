import sys

import pygame as pg
import numpy as np

projectiles = []


class Projectile:
    def __init__(self, starting_pos, direction, speed=10) -> None:
        self.pos = starting_pos
        self.direction = direction
        self.speed = speed


class Boss:
    def __init__(self, starting_pos, starting_angle) -> None:
        self.pos = starting_pos
        self.angle = starting_angle
        self.cannons = np.array(
            [[0, -10, 0], [np.pi / 2, 0, 10], [np.pi, 10, 0], [3 * np.pi / 2, 0, -10]]
        )

    def shoot(self):
        for cannon in self.cannons:
            projectiles.append(Projectile())


BLACK = [0, 0, 0]

WINDOW_SHAPE = [1000, 800]

screen = pg.display.set_mode(WINDOW_SHAPE)


while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    screen.fill(BLACK)

    pg.display.update()
