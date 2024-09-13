
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image

#set the window size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

Window.size = (SCREEN_WIDTH, SCREEN_HEIGHT)


class SpaceInvadersGame(Widget):
    def __init__(self, **kwargs):
        super(SpaceInvadersGame, self).__init__(**kwargs)
        with self.canvas:
            Color(0, 0, 0, 1)
            self.rect = Rectangle(size=(SCREEN_WIDTH, SCREEN_HEIGHT), pos=(0, 0))

        # Add the spaceship image
        self.spaceship = Image(source='static/assets/img/spaceship.png', size=(74, 74),
                               pos=(SCREEN_WIDTH / 2 - 50, 20))
        self.add_widget(self.spaceship)


class SpaceInvadersApp(App):
    def build(self):
        return SpaceInvadersGame()


if __name__ == '__main__':
    SpaceInvadersApp().run()
