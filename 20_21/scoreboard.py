from turtle import Turtle
FONT = ('Courier',12,'normal')
ALIGNMENT = "center"

class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)
    
    def update_score(self):
        self.score += 1
        self.display_score()
    
    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)
