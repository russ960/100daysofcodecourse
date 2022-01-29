import turtle as t
from random import randint, choice
t.colormode(255)

timmy = t.Turtle()

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r,g,b)

my_heading = 0
timmy.speed('fastest')
while my_heading < 360:
    timmy.color(random_color())
    timmy.circle(100)
    my_heading += 5
    timmy.setheading(my_heading)


screen = t.Screen()
screen.exitonclick()