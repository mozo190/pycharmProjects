from scoreboard import Scoreboard
from player import Player
from turtle import Screen

screen = Screen()
player = Player()
scoreboard = Scoreboard()

screen.title("TURTLE CROSSING")
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)
screen.listen()

screen.exitonclick()
