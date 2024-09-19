from kivy.clock import Clock
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

        # schedule the update function
        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def update(self, dt):
        self.ball.move_ball()
        # check for collision of ball with walls
        if self.ball.ball_x < 0 or self.ball.ball_x > self.width - self.ball.WIDTH:
            self.ball.ball_vel_x = -self.ball.ball_vel_x

        if self.ball.ball_y > self.height - self.ball.HEIGHT:
            self.ball.ball_vel_y = -self.ball.ball_vel_y

        if self.ball.ball_y < 0:
            self.ball.ball_vel_y = -self.ball.ball_vel_y


        # self.check_collision()
