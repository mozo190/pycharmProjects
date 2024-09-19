from kivy.properties import NumericProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget


class Bat(Widget):
    bat_x = NumericProperty(400)
    bat_y = NumericProperty(30)

    def __init__(self, **kwargs):
        super(Bat, self).__init__(**kwargs)
        self.WIDTH = 100
        self.HEIGHT = 20
        self.batImage = Image(source='assets/img/bat.bmp')
        self.batImage.size = self.WIDTH, self.HEIGHT
        self.add_widget(self.batImage)

        self.bind(bat_x=self.update_position, bat_y=self.update_position)
        self.update_position()

    def update_position(self, *args):
        self.batImage.pos = self.bat_x, self.bat_y
