from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image


class PlayButton(ButtonBehavior, Image):
    def __init__(self, game, **kwargs):
        super(PlayButton, self).__init__(**kwargs)
        self.game = game
        self.source = 'assets/img/play-button-icon-small.png'
        # self.background_down = 'assets/img/button_press.png'
        self.size_hint = None, None
        self.size = (200, 100)
        self.pos = (300, 170)
        self.allow_stretch = True
        self.keep_ratio = True

        self.bind(on_press=self.on_press)

    def on_press(self):
        self.game.restart_game()
