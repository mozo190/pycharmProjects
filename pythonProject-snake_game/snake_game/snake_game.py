from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.widget import Widget

from snake_game.config import SCREEN_HEIGHT, SCREEN_WIDTH
from snake_game.snake import Snake

Window.size = (SCREEN_WIDTH, SCREEN_HEIGHT)


class SnakeGame(Widget):
    def __init__(self, **kwargs):
        super(SnakeGame, self).__init__(**kwargs)
        self.snake = Snake()
        self.snake.start()
        self.add_widget(self.snake)
        Clock.schedule_interval(self.snake.move, 1.0 / 10.0)
