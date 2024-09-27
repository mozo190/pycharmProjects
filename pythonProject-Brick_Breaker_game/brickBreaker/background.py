from kivy.core.audio import SoundLoader
from kivy.uix.image import Image
from kivy.uix.widget import Widget


class Background(Widget):
    def __init__(self, **kwargs):
        super(Background, self).__init__(**kwargs)

        # initialize background
        self.background_image = Image(source='assets/img/bk.bmp')
        self.background_image.allow_stretch = True
        self.background_image.keep_ratio = False
        self.background_image.size = 800, 600
        self.background_image.pos = 0, 0
        self.add_widget(self.background_image)

        # add background sound
        self.background_sound = SoundLoader.load('assets/audio/game-music-001.wav')
        self.background_sound.loop = True
        self.background_sound.play()

    def stop_music(self):
        self.background_sound.stop()

    def play_music(self):
        self.background_sound.play()

