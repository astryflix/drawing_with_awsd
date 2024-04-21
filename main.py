# --------------------------- #
#            notes            #

# c = clear() / reset()
# space = penup / pendown
# ---------------------------- #

import turtle
t = turtle.Turtle()
t.speed(5)


# variables
penup = False


# functions
def go_clear():
    turtle.clear()
    t.penup()
    turtle.home()
    t.pendown()


def turn_left():
    t.left(10)


def turn_right():
    t.right(10)


def go_forward():
    t.forward(2)


def go_backwards():
    t.back(2)


def pen_toggle():
    global penup
    if penup:
        t.pendown()
        penup = False
    else:
        t.penup()
        penup = True


# keys
turtle.listen()
turtle.onkeypress(turn_left, 'a')
turtle.onkeypress(turn_right, 'd')
turtle.onkeypress(go_forward, 'w')
turtle.onkeypress(go_backwards, 's')
turtle.onkeypress(go_clear, 'c')
turtle.onkeypress(pen_toggle, 'space')

turtle.Screen().tracer(0)

while True:
    turtle.Screen().update()
