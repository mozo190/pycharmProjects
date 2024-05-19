from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.score = 0
        self.goto(-240, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"You have {self.score} score.", align=ALIGNMENT, font=FONT)
