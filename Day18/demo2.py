# from turtle import Turtle
# tim = Turtle()

# import turtle
# tim = turtle.Turtle()

# from turtle import *
# tim = turtle.Turtle()

# from turtle import as t
# tim = t.Turtle()

# if there are modules that are not avaialbe in your standard library, then you can use pip to install the modules that are needed. 

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

for i in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen.exitonclick()