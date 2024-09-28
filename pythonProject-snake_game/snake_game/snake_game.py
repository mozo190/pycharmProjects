from kivy.clock import Clock
from kivy.uix.widget import Widget


class SnakeGame(Widget):
    def __init__(self, **kwargs):
        super(SnakeGame, self).__init__(**kwargs)
        self.snake = Snake()
        self.snake.start()
        self.add_widget(self.snake)
        Clock.schedule_interval(self.snake.move, 1.0 / 10.0)
