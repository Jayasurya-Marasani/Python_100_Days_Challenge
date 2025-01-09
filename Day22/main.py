from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height= 600)
screen.title("Pong")

screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun = r_paddle.go_up, key = "Up")
screen.onkey(fun = r_paddle.go_down, key = "Down")
screen.onkey(fun = l_paddle.go_up, key = "w")
screen.onkey(fun = l_paddle.go_down, key = "s")
game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)
    
    # Detect the collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    # To detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Right Paddle Misses
    if ball.xcor() > 380:
        # Ball Reset
        ball.reset_position()
        scoreboard.l_point()
        
    # Left Paddle Misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()




