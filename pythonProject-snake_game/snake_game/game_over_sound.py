from kivy.core.audio import SoundLoader


class GameOverSound:
    def __init__(self):
        self.sound = SoundLoader.load('assets/sound/8-bit-game-over.wav')

    def play_game_over(self):
        self.sound.play()
