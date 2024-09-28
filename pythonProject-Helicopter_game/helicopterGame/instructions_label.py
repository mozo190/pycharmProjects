from kivy.uix.label import Label
from kivy.uix.widget import Widget

from helicopterGame.config import screenWidth, screenHeight


class InstructionsLabel(Widget):
    def __init__(self, **kwargs):
        super(InstructionsLabel, self).__init__(**kwargs)
        self.instructions = Label(text='Game Over! Press Space to Restart')
        self.instructions.font_size = '25sp'
        self.instructions.pos = screenWidth / 2 - self.instructions.width / 2, screenHeight / 2
        self.add_widget(self.instructions)
