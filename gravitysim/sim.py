import time
from abc import ABC

import pygame

from gravitysim.colors import black


class GravityObject(ABC):

    def __init__(self, pos, speed, acc, mass):
        self._pos = pos
        self._speed = speed
        self._acc = acc
        self._mass = mass

    def update(self, objects, g):
        pass

    def draw(self, game_display):
        pass


class Circle(GravityObject):

    def __init__(self, pos, speed, acc, mass, rad, clr):
        super().__init__(pos, speed, acc, mass)
        self._rad = rad
        self._clr = clr

    def update(self, objects: list[GravityObject], g):
        self._pos = (self._pos[0] + self._speed[0], self._pos[1] + self._speed[1])
        self._speed = (self._speed[0] + self._acc[0], self._speed[1] + self._acc[1])

        for obj in objects:
            if obj is self:
                continue
            self._acc = (
                self._acc[0] + 0 if obj._pos[0] == self._pos[0] else (
                            g * obj._mass / (obj._pos[0] - self._pos[0]) * abs(obj._pos[0] - self._pos[0])),
                self._acc[1] + 0 if obj._pos[1] == self._pos[1] else (
                            g * obj._mass / (obj._pos[1] - self._pos[1]) * abs(obj._pos[1] - self._pos[1]))
            )

    def draw(self, game_display):
        pygame.draw.circle(game_display, self._clr.rgb(), self._pos, self._rad)


class GravitySpace:

    def __init__(self, objects: list[GravityObject] = None, g=0.05, res=(1920, 1080), fps=60, strict=True):
        if objects is None:
            objects = []
        self._objects = objects
        self._res = res
        self._fps = fps
        self._strict = strict

        self._g = g

        pygame.init()
        self._game_display = pygame.display.set_mode(res)
        self._game_display.fill(black.rgb())

        self._pix_ar = pygame.PixelArray(self._game_display)
        self._center = None

    def center(self, obj: GravityObject):
        self._center = obj

    def add_object(self, obj: GravityObject):
        self._objects.append(obj)

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self._game_display.fill(black.rgb())
            for obj in self._objects:
                obj.update(self._objects, self._g)

                if self._center:
                    obj._pos = (
                            obj._pos[0] - self._center._pos[0] + (self._res[0] / 2),
                            obj._pos[1] - self._center._pos[1] + (self._res[1] / 2)
                    )

                if self._strict:
                    if obj._pos[0] < 0 or obj._pos[0] > self._res[0]:
                        obj._speed = (-obj._speed[0], obj._speed[1])
                    if obj._pos[1] < 0 or obj._pos[1] > self._res[1]:
                        obj._speed = (obj._speed[0], -obj._speed[1])


                obj.draw(self._game_display)

            time.sleep(1/self._fps)
            pygame.display.update()

