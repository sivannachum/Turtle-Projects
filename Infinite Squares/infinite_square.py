import turtle

black = (0, 0, 0)
colors = [black]

def draw_infinite_square(starting_position: tuple, starting_length: int, length_decrement:float, angle: float):
    turtle.speed(15)
    turtle.penup()
    turtle.goto(starting_position[0], starting_position[1])
    turtle.width(1)
    turtle.pencolor(colors[0])
    
    turtle.pendown()
    length = starting_length
    number_of_colors = len(colors)
    while (length > 1):
        if number_of_colors == 1:
            turtle.forward(length)
        else:
            draw_with_color_change(length)
        length -= length_decrement
        turtle.left(angle)


def draw_with_color_change(length: int):
    current_color = turtle.pencolor()
    current_color_index = 0
    for index in range(len(colors)):
        if (colors[index] == current_color):
            current_color_index = index
            break
    
    color_segment_length = 15
    total_num_color_changes = length//color_segment_length
    color_changes_made = 0
    while (color_changes_made <= total_num_color_changes):
        turtle.forward(color_segment_length)
        current_color_index = (current_color_index+1)%len(colors)
        current_color = colors[current_color_index]
        turtle.pencolor(current_color)
        color_changes_made += 1

    amount_left_to_draw = length-color_segment_length*total_num_color_changes
    turtle.forward(amount_left_to_draw)

def clear_screen():
    turtle.clear()
    # Bug or feature? After (or before) each square is drawn, turtle.reset() should be called if we want squares to be drawn in the same place each time
    # I like this "bug" though since it keeps things interesting, as square locations can vary if the screen is not cleared between squares, so I've kept it
    turtle.reset()


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
    global colors
    colors = [black]


def change_color_to_rainbow():
    global colors
    red = (255, 0, 0)
    pink = (255, 192, 103)
    yellow = (255, 255, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    purple = (128, 0, 128)
    colors = [red, pink, yellow, green, blue, purple]



turtle.penup()
turtle.colormode(255)
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