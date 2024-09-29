from kivy.uix.label import Label


class Score(Label):
    def __init__(self, **kwargs):
        super(Score, self).__init__(**kwargs)
        self.font_size = 20
        self.color = (0, 0, 0, 1)  # black color

        # initial score text
        self.size_hint = (None, None)
        self.pos = (15, 400)
        self.text = "Score: 0"
