from turtle import Turtle
from random import choice, randrange
import time
from venv import create

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.speed_multiplier = 1
        for _ in range(18):
            self.cars.append(self.create_car())

    def create_car(self):
        self.car = Turtle()
        self.car.shape("square")
        self.car.color(choice(COLORS))
        self.car.shapesize(stretch_wid=1,stretch_len=2)
        self.car.penup()
        self.car.setheading(180)
        self.car.goto(randrange(250,1000,50),randrange(-240,240,25))
        return self.car
        
    def car_move(self):
        for mycar in self.cars:
            if mycar.xcor() <= -340:
                self.cars.remove(mycar)
                self.cars.append(self.create_car())
            else:
                mycar.forward(STARTING_MOVE_DISTANCE)
        time.sleep(.1*self.speed_multiplier)

