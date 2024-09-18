from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget


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


class BrickBreakerApp(App):
    def build(self):
        return BrickBreakerGame()


if __name__ == '__main__':
    BrickBreakerApp().run()
