from kivy.core.audio import SoundLoader


class BackgroundSound:
    def __init__(self):
        self.sound = SoundLoader.load('assets/sound/piano-loops-background.wav')

    def play_background(self):
        self.sound.play()

    def stop_background(self):
        self.sound.stop()