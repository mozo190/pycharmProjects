from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.properties import NumericProperty


class Ball(Widget):
    ball_x = NumericProperty(350)
    ball_y = NumericProperty(300)

    def __init__(self, **kwargs):
        super(Ball, self).__init__(**kwargs)
        self.WIDTH = 30
        self.HEIGHT = 30
        self.ballImage = Image(source='assets/img/ball.bmp')
        self.ballImage.size = self.WIDTH, self.HEIGHT
        self.add_widget(self.ballImage)

        self.bind(ball_x=self.update_position, ball_y=self.update_position)
        self.update_position()

    def update_position(self, *args):
        self.ballImage.pos = self.ball_x, self.ball_y
