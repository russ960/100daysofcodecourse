from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)
screen.listen()
player_scoreboard = Scoreboard()

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

screen_is_on = True
while screen_is_on:
    ball.move_ball()
    screen.update()
    if ball.ycor() > 280 or ball.ycor() < -280:
        print(f"{ball.xcor()},{ball.ycor()}")
        ball.bounce_y()
    print(ball.sleep_time)
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 340:
        ball.ball_reset()
        player_scoreboard.l_point()
    elif ball.xcor() < -340:
        ball.ball_reset()
        player_scoreboard.r_point()


screen.exitonclick()