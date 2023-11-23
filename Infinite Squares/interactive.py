from turtle import penup, goto, write
from draw import clear_screen, draw_user_square as draw
from color import set_color_to_black

starting_length = 300
length_decrement = 10
angle = 75

def draw_user_square():
    clear_screen()
    draw(starting_length, length_decrement, angle)

def interactive_mode():
    setup()
    
    get_starting_length_from_user()
    get_length_decrement_from_user()
    get_angle_from_user()

    print("\nPlease return to the Turtle screen and press D to see your square be drawn!")
    print("Be sure to press R first if you want your square drawn in color. :)")


def setup():
    global starting_length, length_decrement, angle

    clear_screen()
    penup()
    set_color_to_black()
    goto(0, 40)
    write('Please go to the terminal to start your interactive square!', align='center', font=('Georgia', 15, 'normal'))
    goto(0, 0)

    starting_length = 300
    length_decrement = 10
    angle = 75

    print("\nI will ask you for a starting length, length decrement, and an angleforyour infinite \"square\".")
    print("Note that the starting length and length decrement should be ints, whereas the angle can be a float.")

def get_starting_length_from_user():
    global starting_length
    print('\nPlease give me the starting length for your infinite \"square\", or press Enter to sumbit the default (300).')
    try:
        starting_length = int(input() or str(starting_length))
    except ValueError:
        print("Provided starting length value was not an int. Setting to the default...\n")


def get_length_decrement_from_user():
    global length_decrement
    print('\nPlease give me the length decrement for your infinite \"square\", or press Enter to submit the default (10).')
    try:
        length_decrement = int(input() or str(length_decrement))
    except ValueError:
        print("Provided length decrement value was not an int. Setting to the default...\n")


def get_angle_from_user():
    global angle
    print('\nPlease give me the angle for your infinite \"square\", or press Enter to submit the default (75).')
    try:
        angle = float(input() or str(angle))
    except ValueError:
        print("Provided angle value was not a float. Setting to the default...\n")