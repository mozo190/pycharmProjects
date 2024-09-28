from kivy.app import App


class SnakeApp(App):
    def build(self):
        return SnakeGame()


if __name__ == '__main__':
    SnakeApp().run()
