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

def draw_infinite_square(starting_position: tuple, starting_length: int, length_decrement:float, angle: float):
    turtle.speed(25)
    if turtle.pencolor() == "black" or turtle.pencolor() == black:
        turtle.speed(5)
    turtle.penup()
    turtle.goto(starting_position[0], starting_position[1])
    turtle.width(1)

    turtle.pendown()
    length = starting_length
    while (length > 1):
        if turtle.pencolor() == "black" or turtle.pencolor() == black:
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


def clear_screen():
    current_color = turtle.pencolor()
    turtle.clear()
    # Bug or feature? After (or before) each square is drawn, turtle.reset() should be called if we want squares to be drawn in the same place each time
    # I like this "bug" though since it keeps things interesting, as square locations can vary if the screen is not cleared between squares, so I've kept it
    turtle.reset()
    if current_color != black:
        change_color_to_rainbow()


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


def change_color_to_black():
    turtle.pencolor(black)


def change_color_to_rainbow():
    global next_color
    turtle.pencolor(red)
    next_color = "pink"


turtle.penup()
turtle.colormode(255)
turtle.pencolor(black)
turtle.goto(0, 40)
turtle.write('Welcome to the infinite "squares" animator!', align='center', font=('Georgia', 20, 'normal'))
turtle.goto(0, 0)
turtle.write('Please click Space to clear the screen, then click any numbers 1-4 to draw a pre-programmed square.', align='center', font=('Georgia', 10, 'normal'))
turtle.goto(0, -20)
turtle.write('You can click B for squares to be drawn in Black, or R for squares to be drawn in Rainbow colors.', align='center', font=('Georgia', 10, 'normal'))
turtle.goto(0, -40)
turtle.write('You can click buttons as many times as you like.', align='center', font=('Georgia', 10, 'normal'))
turtle.goto(0, 30)

turtle.listen()
turtle.onkey(clear_screen, 'space')
turtle.onkey(draw_first_square, '1')
turtle.onkey(draw_second_square, '2')
turtle.onkey(draw_third_square, '3')
turtle.onkey(draw_fourth_square, '4')
turtle.onkey(change_color_to_black, 'b')
turtle.onkey(change_color_to_rainbow, 'r')

turtle.done()