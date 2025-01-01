# Higher Order Functions and Event Listeners
from turtle import Turtle, Screen

def move_forward():
    tim.forward(50)
tim = Turtle()
screen = Screen()

screen.listen()
# Higher Order Function
screen.onkey(key = "space", fun = move_forward)


screen.exitonclick()