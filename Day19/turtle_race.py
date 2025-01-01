from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=700, height=400)
user_bet = screen.textinput(title = "Make Your Bet", prompt = "Which turtle win the race? Enter a Color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan"]
y_positions = [ -150, -100, -50, 0, 50, 100, 150]
is_race_on = False
all_turtles = []
for i in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x = -330, y = y_positions[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
    
while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10) 
        turtle.forward(random_distance)
        if turtle.xcor() > 330:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            is_race_on = False
screen.exitonclick()