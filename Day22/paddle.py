from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)
        self.speed_mulitplier = 2

    def go_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 20 * self.speed_mulitplier
            self.goto(self.xcor(), new_y)
    
    def go_down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - 20 * self.speed_mulitplier
            self.goto(self.xcor(), new_y)