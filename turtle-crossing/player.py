from turtle import Turtle

STARTING_POSITION = (0, -250)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("red")
        self.goto(STARTING_POSITION)
        self.left(90)

    def move_forward(self):
        new_y = self.ycor() + MOVE_DISTANCE
        # if self.position(self.ycor()) < 280:
        self.goto(self.ycor(), new_y)

    def move_backward(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.ycor(), new_y)

    def back_start(self):
        self.goto(STARTING_POSITION)
