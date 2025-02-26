import turtle
import random
import math

def shape(x, size):
    angle = 180
    modifier = 4
    for i in range(0, size // modifier):
        x.fd(size // modifier)
        x.left(180 / size * modifier)

    for i in range(0, size // modifier):
        x.fd(size // modifier)
        x.right(180 / size * modifier)

# Turtle settings
turtle.bgcolor("#FFDAB9")
t = turtle.Turtle()
t.hideturtle()
t.speed("fastest")
turtle.tracer(0, 0)

import time
# start = input("Waiting for user to start...")
# time.sleep(4)

# Set Constants
length = 180 + 90 + 90
startShift = 0
count = 130
shapeSize = 65
turn = math.ceil((length) / count)

# Main Loop
turns = list(range(startShift, startShift + length, turn))
a = 0
b = len(turns) // 2
for i in range(len(turns)):
    # t.left(i * turn + startShift)
    # t.left(i)
    if i % 2 == 0:
        t.left(turns[a])
        a += 1
    else:
        t.left(turns[b])
        b += 1
    shape(t, shapeSize)

    t.penup()
    t.home()
    t.pendown()
    turtle.update()

# Show drawing
turtle.update()
turtle.done()