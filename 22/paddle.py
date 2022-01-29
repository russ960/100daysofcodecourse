from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self, coords):
        super().__init__()
        self.shape("square")
        self.shapesize(5,1,1)
        self.color("white")
        self.penup()
        self.goto(coords)
    
    def up(self):
        x_pos, y_pos = self.position()
        y_pos += 20
        self.goto(x_pos, y_pos)
    
    def down(self):
        x_pos, y_pos = self.position()
        y_pos -= 20
        self.goto(x_pos, y_pos)

