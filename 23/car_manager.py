from turtle import Turtle
from random import choice
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(choice(COLORS))
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.setheading(180)
        self.goto(300,0)

    def car_move(self):
        self.forward(MOVE_INCREMENT)
        time.sleep(.1)

