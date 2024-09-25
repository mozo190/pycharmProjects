from kivy.uix.image import Image
from kivy.uix.widget import Widget


class Brick(Widget):
    def __init__(self, **kwargs):
        super(Brick, self).__init__(**kwargs)
        self.brick_w = 50
        self.brick_h = 20
        self.no_of_bricks = 0
        self.brick_list = []

    def initialize_bricks(self, rows, cols):
        # add dynamically bricks
        for row in range(rows):
            for col in range(cols):
                x_pos = 50 + col * (self.brick_w + 10)  # 50 is the starting x position
                y_pos = 450 - row * (self.brick_h + 10)  # 450 is the starting y position
                brick = Image(source='assets/img/brick.bmp')
                brick.size = self.brick_w, self.brick_h
                brick.pos = x_pos, y_pos
                self.brick_list.append(brick)
                self.add_widget(brick)
                self.no_of_bricks = rows * cols  # calculate the number of bricks
