from kivy.app import App
from kivy.core.window import Window

from helicopterGame.helicopter_game import HelicopterGame

# screen dimension
screenWidth = 600
screenHeight = 400

# set window size
Window.size = (screenWidth, screenHeight)


class HelicopterApp(App):
    def build(self):
        return HelicopterGame()


if __name__ == '__main__':
    HelicopterApp().run()
