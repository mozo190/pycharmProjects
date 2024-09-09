from kivy.app import App
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.widget import Widget

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 250
DINO_Y_POS = 30

Window.size = (SCREEN_WIDTH, SCREEN_HEIGHT)
Window.clearcolor = (1, 1, 1, 1)


class Ground(Image):
    def __init__(self, **kwargs):
        super(Ground, self).__init__(**kwargs)
        self.source = 'static/assets/img/sprites/ground.png'
        self.size = (1202, 26)
        self.pos = (0, 0)


class Dino(Image):
    def __init__(self, **kwargs):
        super(Dino, self).__init__(**kwargs)
        self.source = 'static/assets/img/sprites/dino_.png'
        self.width, self.height = (44, 48)
        self.size = (self.width, self.height)
        self.pos = (20, DINO_Y_POS)


class DinoGame(Widget):
    def __init__(self, **kwargs):
        super(DinoGame, self).__init__(**kwargs)

        self.ground = Ground()
        self.add_widget(self.ground)

        self.dino = Dino()  # Image(source='dino.png', pos=(100, 0))
        self.add_widget(self.dino)


class DinoApp(App):
    def build(self):
        return DinoGame()


if __name__ == '__main__':
    DinoApp().run()
