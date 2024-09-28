from kivy.uix.image import Image
from kivy.uix.widget import Widget


class Snake(Widget):
    def __init__(self, **kwargs):
        super(Snake, self).__init__(**kwargs)
        self.snake = Image(source='assets/img/snake_.png')
        self.snake.pos = 100, 100
        self.snake.size = 30, 30
        self.add_widget(self.snake)
