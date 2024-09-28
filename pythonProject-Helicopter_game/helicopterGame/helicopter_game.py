from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.widget import Widget

from helicopterGame.helicopter import Helicopter, upward_movement, gravity
from helicopterGame.title_label import TitleLabel


class HelicopterGame(Widget):
    def __init__(self, **kwargs):
        super(HelicopterGame, self).__init__(**kwargs)

        self.player = Helicopter()
        self.add_widget(self.player)

        # add title and instructions to the game
        self.title = TitleLabel()
        self.add_widget(self.title)

        Window.bind(on_key_down=self.key_down)

        Clock.schedule_interval(self.update, 1.0 / 60.0)  # call the update function 60 times per second
        self.game_started = False  # initialize the game_started flag to False

    def update(self, dt):
        if self.game_started:
            self.player.dy += gravity  # apply gravity to the helicopter
            self.player.move_helicopter()

    def key_down(self, window, key, *args):
        if key == 32:  # space key
            self.remove_widget(self.title)
            self.player.start_game()
            self.game_started = True
        elif key == 273 and self.game_started:  # up key
            self.player.dy = upward_movement  # move the helicopter up when the up key is pressed
