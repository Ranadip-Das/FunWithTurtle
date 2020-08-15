# Python program to draw Spiral Helix pattern using Turtle programming.
import turtle

window = turtle.Screen()
turtle.speed(2)
turtle.bgcolor('Black')

for i in range(120):
    turtle.pencolor('Blue')
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)

turtle.exitonclick()