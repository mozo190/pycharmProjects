from kivy.uix.image import Image
from kivy.uix.widget import Widget


class Brick(Widget):
    def __init__(self, **kwargs):
        super(Brick, self).__init__(**kwargs)
        self.brick_w = 50
        self.brick_h = 20
        self.brick_list = []

    def initialize_bricks(self):
        for row in range(450, 551, 50):
            for col in range(50, 651, 100):
                brick = Image(source='assets/img/brick.bmp')
                brick.size = self.brick_w, self.brick_h
                brick.pos = col, row
                self.brick_list.append(brick)
                self.add_widget(brick)
