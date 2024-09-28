from kivy.uix.image import Image
from kivy.uix.widget import Widget


class Snake(Widget):
    def __init__(self, **kwargs):
        super(Snake, self).__init__(**kwargs)
        self.snake = [Image(source='assets/img/snake_.png', size_hint=(None, None), pos=(100, 100), size=(30, 30))]
        self.add_widget(self.snake[0])
