from kivy.uix.image import Image
from kivy.uix.widget import Widget


class GameWin(Widget):
    def __init__(self, **kwargs):
        super(GameWin, self).__init__(**kwargs)
        self.WIDTH = 800
        self.HEIGHT = 600
        self.gox = 30
        self.goy = 50

        self.goImage = Image(source='assets/img/win.bmp')
        self.goImage.size = self.WIDTH, self.HEIGHT
        self.goImage.pos = self.gox, self.goy
        self.add_widget(self.goImage)
        self.goImage.opacity = 0

    def drawImage(self):
        self.goImage.opacity = 1
