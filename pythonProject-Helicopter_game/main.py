from kivy.app import App
from kivy.core.window import Window

from helicopterGame.config import screenWidth, screenHeight
from helicopterGame.helicopter_game import HelicopterGame

# set window size
Window.size = (screenWidth, screenHeight)


class HelicopterApp(App):
    def build(self):
        return HelicopterGame()


if __name__ == '__main__':
    HelicopterApp().run()
