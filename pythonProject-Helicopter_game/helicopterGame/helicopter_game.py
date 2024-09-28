from kivy.uix.widget import Widget

from helicopterGame.helicopter import Helicopter


class HelicopterGame(Widget):
    def __init__(self, **kwargs):
        super(HelicopterGame, self).__init__(**kwargs)

        self.player = Helicopter()
        self.add_widget(self.player)
