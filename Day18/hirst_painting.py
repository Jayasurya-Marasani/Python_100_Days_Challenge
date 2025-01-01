import turtle
import colorgram as cg
import random
from PIL import Image

tim = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)
colors = cg.extract('image.jpg', 20)

rgb_colors = [(colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b) for i in range(len(colors))]

tim.speed(300)
tim.teleport(x = -700 , y = -350 )
for i in range(0, 720, 20):
    tim.teleport(x = -700, y= -350 + i)
    for j in range(0, 1400, 20):
        tim.color(random.choice(rgb_colors))
        tim.dot(10)
        tim.hideturtle()
        tim.penup()
        tim.forward(20)
        tim.pendown()
        tim.hideturtle()

canvas = screen.getcanvas()
canvas.postscript(file="hirst_painting.eps")  # Save the canvas to an EPS file

screen.exitonclick()
img = Image.open("hirst_painting.eps")
img.save("hirst_painting.png")