from kivy.uix.image import Image
from kivy.uix.widget import Widget


class Food(Widget):
    def __init__(self, **kwargs):
        super(Food, self).__init__(**kwargs)
        self.food = Image(source='assets/img/food_.png')
        self.food.size = 18, 18
        self.food.pos = 300, 300
        self.add_widget(self.food)
