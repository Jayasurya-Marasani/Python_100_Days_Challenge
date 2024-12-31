import turtle
import random 
tim = turtle.Turtle()
tim.pensize(10)
turtle.colormode(255)
screen = turtle.Screen()
turtle.colormode(255)
colors = ["red", "blue", "green", "orange", "purple", "pink", "yellow", "cyan"]

# height = screen.window_height()//2
# width = screen.window_width()//2
# print(height, width)
# for i in range(20):
#     choice = random.randint(1, 3)
#     color = random.choice(colors)
#     tim.color(color)
#     if choice == 1:
#         tim.left(90)
#     elif choice == 2:
#         tim.right(90)
#     x, y = tim.pos()
#     x = int(x)  
#     y = int(y)
#     print(x, y)
#     if (-width + 50) < x < (width - 50) and (-height + 50) < y < (height - 50):
#         tim.forward(50)
#     else:
#         tim.left(90)
#         tim.left(90)
#         tim.forward(50)
    
directions = [0, 90, 180, 270]
tim.speed(300)
for _ in range(200):
    tim.speed(20)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    tim.pencolor(color)
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen.exitonclick()