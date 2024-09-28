from kivy.core.audio import SoundLoader
from kivy.core.image import Image as CoreImage
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget

from helicopterGame.config import screenWidth, screenHeight

gravity = 0.05
upward_movement = -1.8


class Helicopter(Widget):
    def __init__(self, **kwargs):
        super(Helicopter, self).__init__(**kwargs)
        self.width = 50
        self.height = 30
        self.x = screenWidth / 2 - self.width / 2
        self.y = screenHeight / 2 - self.height / 2
        self.dy = 0  # initial vertical speed
        self.helicopter_sound = SoundLoader.load('assets/audio/helicopter.wav')

        self.actor_image = CoreImage('assets/img/yellow-cartoon-helicopter.png').texture
        with self.canvas:
            self.rect = Rectangle(texture=self.actor_image)
            self.rect.pos = (self.x, self.y)
            self.rect.size = (self.width, self.height)

    def move_helicopter(self):
        self.y -= self.dy  # move the helicopter up or down
        self.rect.pos = (self.x, self.y)
        self.helicopter_sound.play()

    def reset_position(self):
        self.x = screenWidth / 2 - self.width / 2
        self.y = screenHeight / 2 - self.height / 2
        self.dy = 0
        self.helicopter_sound.stop()

        if hasattr(self, 'rect'):
            self.rect.pos = (self.x, self.y)

    def on_touch_down(self, touch):  # move the helicopter up when the screen is touched
        self.dy = upward_movement  # move the helicopter up
        self.helicopter_sound.play()  # play the helicopter sound
