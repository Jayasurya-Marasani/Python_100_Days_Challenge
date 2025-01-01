import turtle
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)
    
tim = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)
tim.speed("fastest")
size_of_gap = 1
for i in range(360 // size_of_gap):
    tim.color(random_color())
    # tim.circle(100)
    # tim.left(2.5)
    # tim.color(random_color())
    # tim.circle(50)
    tim.circle(100)
    tim.setheading(tim.heading() + size_of_gap)
    
screen.exitonclick()