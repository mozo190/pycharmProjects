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
        screen_width = 800  # Window width dynamically
        total_bricks_width = cols * self.brick_w  # in one line all bricks width
        total_spacing = screen_width - total_bricks_width  # space between bricks
        spacing = total_spacing / (cols + 1)
        # add dynamically bricks
        for row in range(rows):
            for col in range(cols):
                x_pos = spacing + col * (self.brick_w + spacing)  # 50 is the starting x position
                y_pos = 550 - row * (self.brick_h + 10)  # 450 is the starting y position
                brick = Image(source='assets/img/brick.bmp')
                brick.size = self.brick_w, self.brick_h
                brick.pos = x_pos, y_pos
                self.brick_list.append(brick)
                self.add_widget(brick)
                self.no_of_bricks = rows * cols  # calculate the number of bricks
