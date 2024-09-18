
from kivy.app import App

from kivy.uix.image import Image
from kivy.uix.widget import Widget


class BrickBreakerGame(Widget):
    def __init__(self, **kwargs):
        super(BrickBreakerGame, self).__init__(**kwargs)

        #add background image
        self.background = Image(source='assets/img/bk.bmp')
        self.background.allow_stretch = True
        self.background.keep_ratio = False
        self.background.size = 800, 600
        self.background.pos = 0, 0
        self.add_widget(self.background)


class BrickBreakerApp(App):
    def build(self):
        return BrickBreakerGame()


if __name__ == '__main__':
    BrickBreakerApp().run()
