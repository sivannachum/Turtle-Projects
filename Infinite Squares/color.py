import turtle
black = (0, 0, 0)
red = (255, 0, 0)
pink = (231, 85, 128)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (125, 0, 130)
next_color = "pink"


def change_color_to_black():
    turtle.pencolor(black)


def change_color_to_rainbow():
    global next_color
    turtle.pencolor(red)
    next_color = "pink"


def draw_with_color_change(length: int):    
    color_segment_length = 15
    total_num_color_changes = length//color_segment_length
    color_changes_made = 0
    while (color_changes_made <= total_num_color_changes):
        turtle.forward(color_segment_length)
        change_color()
        color_changes_made += 1

    amount_left_to_draw = length-color_segment_length*total_num_color_changes
    turtle.forward(amount_left_to_draw)


def change_color():
    global next_color
    current_color = turtle.pencolor()
    r = int(current_color[0])
    g = int(current_color[1])
    b = int(current_color[2])
    if next_color == "red":
        current_color = (r+5, g, b-5)
        if (current_color == red):
            next_color = "pink" 
    elif next_color == "pink":
        current_color = (r-1, g+3, b+5)
        if (current_color == (227, 84, 140)):
            current_color = pink
            next_color = "orange"
    elif next_color == "orange":
        current_color = (r+1, g+4, b-6)
        if (current_color == (252, 169, 2)):
            current_color = orange
            next_color = "yellow"
    elif next_color == "yellow":
        current_color = (r, g+5, b)
        if (current_color == yellow):
            next_color = "green"
    elif next_color == "green":
        current_color = (r-17, g, b)
        if (current_color == green):
            next_color = "blue"
    elif next_color == "blue":
        current_color = (r, g-5, b+5)
        if (current_color == blue):
            next_color = "purple"
    elif next_color == "purple":
        current_color = (r+5, g, b-5)
        if (current_color == purple):
            next_color = "red" 
    turtle.pencolor(current_color)