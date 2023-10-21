import turtle

def draw_infinite_square(starting_position: tuple, starting_length: int, length_decrement:float, angle: float):
    turtle.speed(15)
    turtle.goto(starting_position[0], starting_position[1])
    turtle.width(1)
    
    turtle.pendown()
    length = starting_length
    while (length > 1):
        turtle.forward(length)
        length -= length_decrement
        turtle.left(angle)
    
    turtle.penup()


def clear_screen():
    turtle.clear()
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


turtle.penup()
turtle.goto(0, 20)
turtle.write('Welcome to the infinite "squares" animator!', align='center', font=('Georgia', 20, 'normal'))
turtle.goto(0, -20)
turtle.write('Please click Space to clear the screen, then click any numbers 1-4 to draw a pre-programmed square.', align='center', font=('Georgia', 10, 'normal'))
turtle.goto(0, -40)
turtle.write('You can click buttons as many times as you like.', align='center', font=('Georgia', 10, 'normal'))
turtle.goto(0, 10)

turtle.listen()
turtle.onkey(clear_screen, 'space')
turtle.onkey(draw_first_square, '1')
turtle.onkey(draw_second_square, '2')
turtle.onkey(draw_third_square, '3')
turtle.onkey(draw_fourth_square, '4')

turtle.done()