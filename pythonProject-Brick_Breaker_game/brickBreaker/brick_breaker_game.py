from kivy.uix.image import Image
from kivy.uix.widget import Widget

from .ball import Ball
from .bat import Bat
from .brick import Brick


class BrickBreakerGame(Widget):
    def __init__(self, **kwargs):
        super(BrickBreakerGame, self).__init__(**kwargs)

        # add background image
        self.background = Image(source='assets/img/bk.bmp')
        self.background.allow_stretch = True
        self.background.keep_ratio = False
        self.background.size = 800, 600
        self.background.pos = 0, 0
        self.add_widget(self.background)

        # add ball
        self.ball = Ball()
        self.add_widget(self.ball)

        # add bat
        self.bat = Bat()
        self.add_widget(self.bat)

        # add bricks
        self.bricks = Brick()
        self.add_widget(self.bricks)
        self.bricks.initialize_bricks()
