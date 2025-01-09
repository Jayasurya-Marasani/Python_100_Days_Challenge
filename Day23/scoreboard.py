from turtle import Turtle


FONT = ("JetBrainsMono Nerd Font", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()    
        self.hideturtle()
        self.penup()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-250, 250)
        self.write(f"Level: {self.level}", align = "left", font = FONT )

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align= "center", font = FONT)
        # self.clear()
        # self.write(f"Your Level = {self.level}", align="center", font = FONT)