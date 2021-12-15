import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(player.move_up, 'Up')

car = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
    if player.is_at_finish_line():
        player.go_back_to_starting_position()
        car.level_up()
        scoreboard.level_increase()

screen.exitonclick()