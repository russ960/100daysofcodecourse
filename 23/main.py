from sys import platlibdir
import time
from turtle import Screen, Turtle, onkeypress
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

def write_score(score):
    screen_text.clear()
    screen_text.goto(-240,280)
    screen_text.write(f"Level: {score}", align="right", font=FONT)

screen = Screen()
player = Player()
screen_text = Turtle()

screen_text.color("black")
screen_text.penup()
screen_text.ht()
FONT = ('Arial',12,'normal')

screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.bgcolor("white")
screen.onkey(player.move_turtle,"Up")

car = CarManager()

level = 1
write_score(level)

game_is_on = True
while game_is_on:
    
    car.car_move()
    for c in car.cars:
        if player.distance(c) < 20:
            game_is_on = False
            screen_text.goto(0,0)
            screen_text.write("GAME OVER", align="center", font=FONT)

    if player.ycor() == 280.0:
        screen.update()
        time.sleep(0.5)
        player.update_level()
        car.speed_multiplier *= .6
        level += 1
        write_score(level)
        

    screen.update()
screen.exitonclick()