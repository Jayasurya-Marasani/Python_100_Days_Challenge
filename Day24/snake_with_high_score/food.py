from turtle import Turtle, Screen
import time
import random

class Food(Turtle):
    
    def __init__(self):
       super().__init__() 
       self.shape("circle")
       self.penup()
       self.shape("turtle")
    #    self.shapesize(stretch_len = 1, stretch_wid = 1)
       self.color("yellow")
       self.speed("fastest")
       self.refresh()

    def refresh(self):
       self.random_x = random.randint(-280, 280)
       self.random_y = random.randint(-280, 280)
       self.goto(self.random_x, self.random_y)
      


