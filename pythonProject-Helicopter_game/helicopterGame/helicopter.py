from kivy.core.image import Image as CoreImage
from kivy.uix.widget import Widget

from main import screenWidth, screenHeight


class Helicopter(Widget):
    def __init__(self, **kwargs):
        super(Helicopter, self).__init__(**kwargs)
        self.width = 50
        self.height = 30
        self.x = screenWidth / 2 - self.width / 2
        self.y = screenHeight / 2 - self.height / 2

        self.actor_image = CoreImage('assets/img/actor.gif')
