from kivy.uix.widget import Widget

from helicopterGame.helicopter import Helicopter
from helicopterGame.title_label import TitleLabel


class HelicopterGame(Widget):
    def __init__(self, **kwargs):
        super(HelicopterGame, self).__init__(**kwargs)

        self.player = Helicopter()
        self.add_widget(self.player)

        # add title and instructions to the game
        self.title = TitleLabel()
        self.add_widget(self.title)
