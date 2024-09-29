from kivy.core.audio import SoundLoader


class BitingSound:
    def __init__(self):
        self.sound = SoundLoader.load('assets/sound/eating-an-apple.wav')

    def play_biting(self):
        self.sound.play()

    def stop_biting(self):
        self.sound.stop()