from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("red")
        self.goto(0, -250)
        self.left(90)

    def move_forward(self):
        new_y = self.ycor() + 10
        self.goto(self.ycor(), new_y)

    def move_backward(self):
        new_y = self.ycor() - 10
        self.goto(self.ycor(), new_y)
