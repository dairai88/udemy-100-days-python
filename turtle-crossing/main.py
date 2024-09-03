"""turtle crossing"""
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

SCREEN = Screen()
SCREEN.setup(width=600, height=600)
SCREEN.tracer(0)

player = Player()
car_manager = CarManager()
score_board = ScoreBoard()

SCREEN.listen()
SCREEN.onkey(player.go_up, "Up")

game_is_on = True # pylint: disable=invalid-name
while game_is_on:
    time.sleep(0.1)
    SCREEN.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False # pylint: disable=invalid-name
            score_board.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        score_board.increase_level()

SCREEN.exitonclick()
