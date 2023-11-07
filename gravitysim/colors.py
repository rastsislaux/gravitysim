from abc import ABC


class Color(ABC):

    def rgb(self):
        pass


class Black(Color):

    def rgb(self):
        return 0, 0, 0


class White(Color):

    def rgb(self):
        return 255, 255, 255


class Green(Color):

    def rgb(self):
        return 0, 255, 0


black = Black()
white = White()
green = Green()
