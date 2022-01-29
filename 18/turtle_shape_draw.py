from turtle import Turtle, Screen
from random import choice
import turtle
color_list = ["black", "blue", "navy", "green", "red", "indigo", "pink", "blue violet"]
timmy = Turtle()
timmy.penup()
#timmy.setx(180.0)
timmy.sety(180.0)
timmy.pendown()

for side_count in range(3,11):
    timmy.pencolor(choice(color_list))
    
    calc_angle = 360 / side_count
    for i in range(side_count):
        timmy.forward(100)
        timmy.right(calc_angle)

screen = Screen()
screen.exitonclick()