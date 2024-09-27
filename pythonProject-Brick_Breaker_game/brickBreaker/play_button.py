from kivy.uix.button import Button


class PlayButton(Button):
    def __init__(self, **kwargs):
        super(PlayButton, self).__init__(**kwargs)
        self.play_button = 'assets/img/play-button-icon.png'
        self.size_hint = None, None
        self.size = 200, 100
        self.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
