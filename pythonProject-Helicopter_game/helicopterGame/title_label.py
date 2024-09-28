from kivy.uix.label import Label
from kivy.uix.widget import Widget

from helicopterGame.config import screenWidth, screenHeight


class TitleLabel(Widget):
    def __init__(self, **kwargs):
        super(TitleLabel, self).__init__(**kwargs)
        self.title = Label(text='HELICOPTER GAME')
        self.title.font_size = '25sp'
        self.title.pos = screenWidth / 2 - self.title.width / 2, screenHeight - 100
        self.add_widget(self.title)
        self.instructions = Label(text='Press SPACE to start')
        self.instructions.font_size = '25sp'
        self.instructions.pos = screenWidth / 2 - self.instructions.width / 2, screenHeight / 2
        self.add_widget(self.instructions)
