from turtle import Turtle, Screen
ALIGNMENT = "center"
FONT = ("JetBrainsMono Nerd Font", 16, "bold")
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode = "r") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score = {self.score}\tHighScore = {self.high_score}", align=ALIGNMENT, font=FONT)
    
    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score}\tHighScore = {self.high_score}", align=ALIGNMENT, font= FONT)
    
    def increase_score(self):
        self.score += 1 

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align = ALIGNMENT, font = FONT)
    #     self.goto(0, -23)
    #     self.write(f"Your Score = {self.score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode = "w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_score()
        

