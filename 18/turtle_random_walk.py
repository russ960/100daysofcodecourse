import turtle as t
from random import randint, choice
t.colormode(255)

#color_list = ["black", "blue", "navy", "green", "red", "indigo", "pink", "blue violet"]
timmy = t.Turtle()

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r,g,b)

def random_turn_move():
#    direction = randint(0,1)
#    if direction == 0:
#        timmy.right(90)
#    if direction == 1:
#        timmy.left(90)
    direction = [0, 90, 180, 270]
    timmy.setheading(choice(direction))
    timmy.color(random_color())
    timmy.forward(50)
timmy.hideturtle()
timmy.pensize(10)
timmy.speed(10)
for _ in range(200):
    random_turn_move()

screen = t.Screen()
screen.exitonclick()