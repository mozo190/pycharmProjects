from kivy.app import App
from kivy.core.window import Window

Window.size = (800, 600)


class BrickBreakerGame:
    pass


class BrickBreakerApp(App):
    def build(self):
        return BrickBreakerGame()


if __name__ == '__main__':
    BrickBreakerApp().run()
