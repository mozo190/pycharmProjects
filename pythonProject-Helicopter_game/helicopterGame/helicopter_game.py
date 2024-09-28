from kivy.uix.widget import Widget

from helicopterGame.helicopter import Helicopter


class HelicopterGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.helicopter = Helicopter()
        self.add_widget(self.helicopter)
