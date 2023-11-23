from turtle import pencolor
from typing import Union

__black = (0, 0, 0)
__red = (255, 0, 0)
__pink = (231, 85, 128)
__orange = (255, 165, 0)
__yellow = (255, 255, 0)
__green = (0, 255, 0)
__blue = (0, 0, 255)
__purple = (125, 0, 130)
__next_color = "pink"

def color_is_black(color: Union[tuple, str]):
    return color == "black" or color == __black


def get_black():
    return __black


def get_rainbow_color():
    global __next_color
    __next_color = "pink"
    return __red


def get_new_pen_color(current_color: tuple):
    global __next_color
    r = int(current_color[0])
    g = int(current_color[1])
    b = int(current_color[2])
    new_color = current_color
    if __next_color == "red":
        new_color = (r+5, g, b-5)
        if (new_color == __red):
            __next_color = "pink" 
    elif __next_color == "pink":
        new_color = (r-1, g+3, b+5)
        if (new_color == (227, 84, 140)):
            new_color = __pink
            __next_color = "orange"
    elif __next_color == "orange":
        new_color = (r+1, g+4, b-6)
        if (new_color == (252, 169, 2)):
            new_color = __orange
            __next_color = "yellow"
    elif __next_color == "yellow":
        new_color = (r, g+5, b)
        if (new_color == __yellow):
            __next_color = "green"
    elif __next_color == "green":
        new_color = (r-17, g, b)
        if (new_color == __green):
            __next_color = "blue"
    elif __next_color == "blue":
        new_color = (r, g-5, b+5)
        if (new_color == __blue):
            __next_color = "purple"
    elif __next_color == "purple":
        new_color = (r+5, g, b-5)
        if (new_color == __purple):
            __next_color = "red" 
    return new_color


def set_color_to_black():
    pencolor(get_black())


def set_color_to_rainbow():
    pencolor(get_rainbow_color())