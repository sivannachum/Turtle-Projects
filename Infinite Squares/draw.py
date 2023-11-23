import turtle
from color import get_new_pen_color, color_is_black, set_color_to_rainbow

def draw_infinite_square(starting_position: tuple, starting_length: int, length_decrement: float, angle: float):
    turtle.speed(25)
    if color_is_black(turtle.pencolor()):
        turtle.speed(5)
    turtle.penup()
    turtle.goto(starting_position[0], starting_position[1])
    turtle.width(1)

    turtle.pendown()
    length = starting_length
    while (length > 1):
        if color_is_black(turtle.pencolor()):
            turtle.forward(length)
        else:
            draw_with_color_change(length)
        length -= length_decrement
        turtle.left(angle)


def draw_with_color_change(length: int):    
    color_segment_length = 15
    total_num_color_changes = length//color_segment_length
    color_changes_made = 0
    while (color_changes_made <= total_num_color_changes):
        turtle.forward(color_segment_length)
        current_color = turtle.pencolor()
        new_color = get_new_pen_color(current_color)
        turtle.pencolor(new_color)
        color_changes_made += 1

    amount_left_to_draw = length-color_segment_length*total_num_color_changes
    turtle.forward(amount_left_to_draw)


def clear_screen():
    current_color = turtle.pencolor()
    turtle.clear()
    # Bug or feature? After (or before) each square is drawn, turtle.reset() should be called if we want squares to be drawn in the same place each time
    # I like this "bug" though since it keeps things interesting, as square locations can vary if the screen is not cleared between squares, so I've kept it
    turtle.reset()
    if not color_is_black(current_color):
        set_color_to_rainbow()


def draw_first_square():
    draw_infinite_square((0, -turtle.window_height() + 20), turtle.window_height() - 40, 1, 89)


def draw_second_square():
    starting_position = (-turtle.window_width()/3, -turtle.window_height()/3)
    starting_length = turtle.window_height() - 180
    length_decrement = 1
    angle = 91
    draw_infinite_square(starting_position, starting_length, length_decrement, angle)


def draw_third_square():
    starting_position = (-turtle.window_width()/3, -turtle.window_height()/3 + 20)
    starting_length = turtle.window_height() - 180
    length_decrement = 1
    angle = 100
    draw_infinite_square(starting_position, starting_length, length_decrement, angle)


def draw_fourth_square():
    starting_position = (-turtle.window_width()/3, -turtle.window_height()/3 + 20)
    starting_length = turtle.window_height() - 180
    length_decrement = 3
    angle = 90.3
    draw_infinite_square(starting_position, starting_length, length_decrement, angle)


def draw_user_square(starting_length: int, length_decrement: int, angle: float):
    starting_position = (-turtle.window_width()/3, -turtle.window_height()/3 + 20)
    starting_length = starting_length
    draw_infinite_square(starting_position, starting_length, length_decrement, angle)