from turtle import Turtle, Screen

timmy = Turtle()
line_size = 0
while line_size < 100:
    timmy.forward(8)
    timmy.penup()
    timmy.forward(2)
    timmy.pendown()
    line_size += 10

screen = Screen()
screen.exitonclick()