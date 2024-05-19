import time

from scoreboard import Scoreboard
from player import Player
from turtle import Screen

screen = Screen()
player = Player()
scoreboard = Scoreboard()


def stop_game():
    global game_is_on
    game_is_on = False


screen.title("TURTLE CROSSING")
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

screen.listen()
screen.onkey(player.move_forward(), "Up")
screen.onkey(player.move_backward(), "Down")

screen.onkey(stop_game, "q")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
