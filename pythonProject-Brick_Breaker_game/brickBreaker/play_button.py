from kivy.uix.button import Button


class PlayButton(Button):
    def __init__(self, **kwargs):
        super(PlayButton, self).__init__(**kwargs)
        self.background_normal = 'assets/img/play-button-icon-small.png'
        self.background_down = 'assets/img/button_press.png'
        self.size_hint = None, None
        self.size = 200, 100
        self.pos = 300, 170
        self.allow_stretch = True
        self.keep_ratio = False

        self.bind(on_press=self.on_press)

    def on_press(self):
        print("Play button pressed!")
