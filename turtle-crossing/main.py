import time

from scoreboard import Scoreboard
from player import Player
from turtle import Screen
from car_manager import CarManager

screen = Screen()
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


def stop_game():
    global game_is_on
    game_is_on = False


screen.title("TURTLE CROSSING")
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

screen.listen()
screen.onkey(player.move_forward, "Up")

screen.onkey(stop_game, "q")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.back_start()
        car_manager.level_up()
        scoreboard.increase_score()

screen.exitonclick()
