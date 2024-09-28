from kivy.app import App

from helicopterGame.helicopter_game import HelicopterGame


class HelicopterApp(App):
    def build(self):
        return HelicopterGame()


if __name__ == '__main__':
    HelicopterApp().run()
