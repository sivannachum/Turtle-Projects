import turtle
from color import set_color_to_black, set_color_to_rainbow
from draw import *
from interactive import interactive_mode, draw_user_square

def give_instructions():
    clear_screen()
    set_color_to_black()
    turtle.penup()
    turtle.goto(0, 40)
    turtle.write('Welcome to the infinite "squares" animator!', align='center', font=('Georgia', 20, 'normal'))
    turtle.goto(0, 0)
    turtle.write('Please click Space to clear the screen, then click any numbers 1-4 to draw a pre-programmed square.', align='center', font=('Georgia', 10, 'normal'))
    turtle.goto(0, -20)
    turtle.write('You can click B for squares to be drawn in Black, or R for squares to be drawn in Rainbow colors.', align='center', font=('Georgia', 10, 'normal'))
    turtle.goto(0, -40)
    turtle.write('Lastly, you can click I to start interactive mode and design your own infinite "square".', align='center', font=('Georgia', 10, 'normal'))
    turtle.goto(0, -60)
    turtle.write('You can click buttons as many times as you like, and press H to bring this screen back up.', align='center', font=('Georgia', 10, 'normal'))
    turtle.penup()
    turtle.goto(0, 30)


turtle.colormode(255)
give_instructions()
turtle.listen()
turtle.onkey(give_instructions, 'h')
turtle.onkey(clear_screen, 'space')
turtle.onkey(draw_first_square, '1')
turtle.onkey(draw_second_square, '2')
turtle.onkey(draw_third_square, '3')
turtle.onkey(draw_fourth_square, '4')
turtle.onkey(set_color_to_black, 'b')
turtle.onkey(set_color_to_rainbow, 'r')
turtle.onkey(interactive_mode, 'i')
turtle.onkey(draw_user_square, 'd')

turtle.done()
