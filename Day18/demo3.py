from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

shapes = {"Triangle": 3, "Square": 4, "Pentagon": 5, "Hexagon": 6,
          "Heptagon": 7, "Octagon": 8, "Nonagon": 9, "Decagon": 10}
colors = ["red", "blue", "green", "orange", "purple", "pink", "yellow", "cyan"]
for i, (shape, sides) in enumerate(shapes.items()):
    tim.color(colors[i % len(colors)])
    external_angle = 360 // sides
    for _ in range(sides):
        tim.forward(100)
        tim.right(external_angle)

screen.exitonclick()
