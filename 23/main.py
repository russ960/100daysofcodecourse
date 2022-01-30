from sys import platlibdir
import time
from turtle import Screen, onkeypress
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.bgcolor("white")
screen.onkey(player.move_turtle,"Up")

car = CarManager()

game_is_on = True
while game_is_on:
    screen.update()
    car.car_move()
    if player.ycor() == 280.0:
        screen.update()
        time.sleep(0.5)
        player.update_level()
screen.exitonclick()