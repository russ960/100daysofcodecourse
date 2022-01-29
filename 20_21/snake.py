from turtle import Turtle
import time

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for part in range(3):
            self.add_segment(part)
    
    def add_segment(self, position):
        position = Turtle(shape="square")
        position.color("white")
        position.penup()
        position.goto(x=len(self.snake_body)*-20, y=0)
        self.snake_body.append(position)
    
    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        time.sleep(.1)
        for seg_num in range(len(self.snake_body)-1,0,-1):
            new_x = self.snake_body[seg_num-1].xcor()
            new_y = self.snake_body[seg_num-1].ycor()
            self.snake_body[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

