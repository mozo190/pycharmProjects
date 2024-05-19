from turtle import Turtle

COLORS = ["red", "green", "yellow", "blue", "orange", "pink", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("orange")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(position)
        self.x_move = MOVE_INCREMENT
        self.move_speed = 0.1

    def move(self):
        new_y = self.xcor() + self.x_move
        self.goto(0, new_y)

