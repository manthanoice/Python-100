from turtle import *
from paddle import *
from ball import *
from scoreboard import *
import time

screen = Screen()

the_list = [(350, 0), (-350, 0)]


screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('🏓 Pong')
screen.tracer(0)

paddle = Paddle(the_list[0])
paddle2 = Paddle(the_list[1])
screen.listen()
screen.onkey(paddle.go_up, 'Up')
screen.onkey(paddle.go_down, 'Down')

screen.onkey(paddle2.go_up, 'w')
screen.onkey(paddle2.go_down, 's')

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
 
while game_is_on:
    time.sleep(0.07)
    screen.update()
    ball.move()
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()
    
    if ball.distance(paddle) < 50 and ball.xcor() > 340 or ball.distance(paddle2) < 50 and ball.xcor() < -340:
        ball.bounce_x()
 
    #When Right side person misses
    if ball.xcor() > 370:
        ball.reset_position()
        scoreboard.increase_left_score()

    #When Left side perosn misses
    if ball.xcor() < -370:
        ball.reset_position()
        scoreboard.increase_right_score()

screen.exitonclick()