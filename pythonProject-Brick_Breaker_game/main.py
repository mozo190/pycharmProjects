from kivy.app import App
from brickBreaker.brick_breaker_game import BrickBreakerGame


class BrickBreakerApp(App):
    def build(self):
        return BrickBreakerGame()


if __name__ == '__main__':
    BrickBreakerApp().run()
