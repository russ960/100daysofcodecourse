# import colorgram

# colors = colorgram.extract('C:\\dev\\playground\\100DaysOfCodePython_Udemy\\18\\image.png',10)

# def get_color_tuple(colors_extract):
#     color_tuple_list = []
#     for color in colors_extract:
#         color_tuple_list.append((color.rgb.r, color.rgb.g, color.rgb.b))
#     return color_tuple_list

# #print(get_color_tuple(colors))
# test = get_color_tuple(colors)
# print(test[0][0], test[0][1], test[0][2])
import turtle as t
from random import choice
t.colormode(255)
timmy = t.Turtle()
color_list = [(41, 104, 174), (234, 205, 114), (228, 151, 85), (189, 46, 74), (231, 118, 144), (115, 90, 46)]

timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(250)
timmy.setheading(0)

for y in range(10):
    for x in range (10):
        timmy.dot(20,choice(color_list))
        if x < 9:
            timmy.forward(50)
    print(timmy.heading())
    if timmy.heading() == 0.0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
    elif timmy.heading() == 180.0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(0)


screen = t.Screen()
screen.exitonclick()


