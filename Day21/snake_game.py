from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import Scoreboard
snake = Snake()
food = Food()
screen = Screen()
scoreboard = Scoreboard()

screen.setup(width= 600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


screen.listen()
screen.onkey(key = "Up", fun = snake.up)
screen.onkey(key = "Down", fun = snake.down)
screen.onkey(key = "Left", fun = snake.left)
screen.onkey(key = "Right", fun = snake.right)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Collision with food
    # can use distance method in turtle

    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.increase_score()
        scoreboard.update_score()
        snake.extend()
    # Detect Collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # Detect Collision with tail
    # if head collides with any segment in the tail:
        # trigger game_over
    
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()