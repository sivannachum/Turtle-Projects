import turtle
from color import black, change_color_to_black, change_color_to_rainbow
from draw import *

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