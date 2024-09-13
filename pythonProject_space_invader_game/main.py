from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image
from kivy.uix.widget import Widget

# set the window size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 1.0 / 60.0

Window.size = (SCREEN_WIDTH, SCREEN_HEIGHT)


class SpaceInvadersGame(Widget):
    def __init__(self, **kwargs):
        super(SpaceInvadersGame, self).__init__(**kwargs)
        with self.canvas:
            Color(0, 0, 0, 1)
            self.rect = Rectangle(size=(SCREEN_WIDTH, SCREEN_HEIGHT), pos=(0, 0))

        # Add the spaceship image
        # self.spaceship = Image(source='static/assets/img/spaceship.png', size=(74, 74),
        #                        pos=(SCREEN_WIDTH / 2 - 50, 20))
        self.spaceship = Image(source='static/assets/img/spaceship.png')
        self.spaceship.size_hint = (None, None)
        self.spaceship.size = (74, 74)
        self.spaceship.pos = (SCREEN_WIDTH / 2 - self.spaceship.width / 2, 20)
        self.add_widget(self.spaceship)

        # bind keyboard events
        Window.bind(on_key_down=self.on_key_down)
        Window.bind(on_key_up=self.on_key_up)

        self.left_pressed = False
        self.right_pressed = False

        Clock.schedule_interval(self.update, FPS)

    def on_key_down(self, window, key, *args):
        if key == 276:  # left arrow key
            self.left_pressed = True
        elif key == 275:  # right arrow key
            self.right_pressed = True

    def on_key_up(self, window, key, *args):
        if key == 276:
            self.left_pressed = False
        elif key == 275:
            self.right_pressed = False

    def update(self, dt):
        if self.left_pressed:
            self.spaceship.x -= 5  # move the spaceship to the left
        elif self.right_pressed:
            self.spaceship.x += 5  # move the spaceship to the right


class SpaceInvadersApp(App):
    def build(self):
        return SpaceInvadersGame()


if __name__ == '__main__':
    SpaceInvadersApp().run()
