# Python program to draw Rainbow Benzene using Turtle programming.

import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
turtle.pen()
turtle.bgcolor('black')

for x in range(360):
    turtle.pencolor(colors[x%6])
    turtle.width(x//6)
    turtle.forward(x)
    turtle.left(45)
