from turtle import Turtle, forward
import time
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.setheading(90)
        self.update_level()

    def move_turtle(self):
        if self.ycor() < FINISH_LINE_Y:
            self.forward(20)
        else:
            time.sleep(1)
            self.update_level()

    def update_level(self):
        self.goto(STARTING_POSITION)