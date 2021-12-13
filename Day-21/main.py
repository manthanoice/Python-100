from turtle import *
from typing_extensions import ParamSpec
from snake import *
from food import *
from scoreboard import *
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("The 🐍😈")
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.09)
    snake.move()
    if snake.head.distance(food) < 13:
        scoreboard.increase_scoreboard()
        snake.extend_snake()
        food.refresh()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.game_over()
        game_is_on = False
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 8:
            game_is_on = False
            scoreboard.game_over()
        


screen.exitonclick()