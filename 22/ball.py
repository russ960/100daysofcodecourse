from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.sleep_time = 0.1

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        time.sleep(self.sleep_time)

    
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.sleep_time *= 0.9

    def ball_reset(self):
        self.goto(0,0)
        self.bounce_x()
        self.sleep_time = 0.1
