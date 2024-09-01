"""pong game"""
from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

SCREEN = Screen()
SCREEN.bgcolor("black")
SCREEN.setup(width=800, height=600)
SCREEN.title("Pong")
SCREEN.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

SCREEN.listen()
SCREEN.onkey(r_paddle.go_up, "Up")
SCREEN.onkey(r_paddle.go_down, "Down")
SCREEN.onkey(l_paddle.go_up, "w")
SCREEN.onkey(l_paddle.go_down, "s")

game_is_on = True # pylint: disable=invalid-name
while game_is_on:
    time.sleep(ball.move_speed)
    SCREEN.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Needs to bounce
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or \
        ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

SCREEN.exitonclick()
