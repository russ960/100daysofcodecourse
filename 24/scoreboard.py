from turtle import Turtle
FONT = ('Courier',12,'normal')
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.display_score()

    def display_score(self):
        self.clear()
        with open(".\\24\\data.txt", mode='r') as hs_file:
            read_high_score = hs_file.read()
            if read_high_score == '':
                self.high_score = 0
            else: 
                self.high_score = int(read_high_score)
            #print(hs_file.read())
                            
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
    
    def update_score(self):
        self.score += 1
        self.display_score()
    
    def reset(self):
        if self.score  > self.high_score:
            self.high_score = self.score
            with open(".\\24\\data.txt", mode='w') as hs_file:
                hs_file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)
