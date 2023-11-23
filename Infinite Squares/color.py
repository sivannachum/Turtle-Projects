from turtle import pencolor
black = (0, 0, 0)
red = (255, 0, 0)
pink = (231, 85, 128)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (125, 0, 130)
next_color = "pink"

def color_is_black(color):
    return color == "black" or color == black


def get_black():
    return black


def get_rainbow_color():
    global next_color
    next_color = "pink"
    return red


def get_new_pen_color(current_color):
    global next_color
    r = int(current_color[0])
    g = int(current_color[1])
    b = int(current_color[2])
    new_color = current_color
    if next_color == "red":
        new_color = (r+5, g, b-5)
        if (new_color == red):
            next_color = "pink" 
    elif next_color == "pink":
        new_color = (r-1, g+3, b+5)
        if (new_color == (227, 84, 140)):
            new_color = pink
            next_color = "orange"
    elif next_color == "orange":
        new_color = (r+1, g+4, b-6)
        if (new_color == (252, 169, 2)):
            new_color = orange
            next_color = "yellow"
    elif next_color == "yellow":
        new_color = (r, g+5, b)
        if (new_color == yellow):
            next_color = "green"
    elif next_color == "green":
        new_color = (r-17, g, b)
        if (new_color == green):
            next_color = "blue"
    elif next_color == "blue":
        new_color = (r, g-5, b+5)
        if (new_color == blue):
            next_color = "purple"
    elif next_color == "purple":
        new_color = (r+5, g, b-5)
        if (new_color == purple):
            next_color = "red" 
    return new_color


def set_color_to_black():
    pencolor(get_black())


def set_color_to_rainbow():
    pencolor(get_rainbow_color())