from turtle import Turtle, Screen, color
import turtle
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?  Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [125,75,25,-25,-75,-125]
all_turtles = []
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("Congratulations you have won!")
            else:
                print(f"Sorry you have lost. {winning_color} won the race!")
        random_distance = randint(0,10)
        turtle.forward(random_distance)
        
        

screen.exitonclick()