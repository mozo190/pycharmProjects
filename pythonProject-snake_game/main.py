from kivy.app import App

from snake_game.snake_game import SnakeGame


class SnakeApp(App):
    def build(self):
        return SnakeGame()


if __name__ == '__main__':
    SnakeApp().run()
