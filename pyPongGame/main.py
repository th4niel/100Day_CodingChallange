from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PyPong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle  = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.Up, "Up")
screen.onkey(r_paddle.Down, "Down")
screen.onkey(l_paddle.Up, "w")
screen.onkey(l_paddle.Down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.r_point()

    #Detect Lpaddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.l_point()

screen.exitonclick()