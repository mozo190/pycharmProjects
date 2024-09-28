import random

from kivy.graphics import Rectangle
from kivy.uix.widget import Widget

from helicopterGame.config import screenHeight, screenWidth

SPEED = -2


class Obstacle(Widget):
    def __init__(self, gap, **kwargs):
        super(Obstacle, self).__init__(**kwargs)
        self.width = 30
        max_height = screenHeight - gap
        min_height = max(0, random.randint(self.width, max_height - self.width * 2))
        self.height_top = random.randint(min_height, max_height - self.width)
        self.height_bottom = max_height - self.height_top
        self.x = screenWidth
        self.y_top = screenHeight - self.height_top
        self.y_bottom = 0
        self.dx = SPEED  # initial horizontal speed

        with self.canvas:
            self.rect_top = Rectangle(pos=(self.x, self.y_top), size=(self.width, self.height_top))
            self.rect_bottom = Rectangle(pos=(self.x, self.y_bottom), size=(self.width, self.height_bottom))