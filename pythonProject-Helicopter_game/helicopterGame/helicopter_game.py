from kivy.uix.label import Label
from kivy.uix.widget import Widget

from helicopterGame.config import screenWidth, screenHeight
from helicopterGame.helicopter import Helicopter


class HelicopterGame(Widget):
    def __init__(self, **kwargs):
        super(HelicopterGame, self).__init__(**kwargs)

        self.player = Helicopter()
        self.add_widget(self.player)

        #add title and instructions to the game
        self.title = Label(text='HELICOPTER GAME')
        self.title.font_size = '25sp'
        self.title.pos = screenWidth / 2 - self.title.width / 2 - 200, screenHeight - 100
        self.add_widget(self.title)
        self.instructions = Label(text='Press SPACE to start')
        self.instructions.font_size = '25sp'
        self.instructions.pos = screenWidth / 2 - 150, screenHeight / 2
        self.add_widget(self.instructions)
