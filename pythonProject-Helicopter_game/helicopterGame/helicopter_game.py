import random
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.widget import Widget

from helicopterGame.helicopter import Helicopter, upward_movement, gravity
from helicopterGame.obstacle import Obstacle
from helicopterGame.title_label import TitleLabel


class HelicopterGame(Widget):
    def __init__(self, **kwargs):
        super(HelicopterGame, self).__init__(**kwargs)

        self.player = Helicopter()
        self.add_widget(self.player)
        self.obstacles = [] # list to store obstacles widgets
        self.min_gap = self.player.height * 4  # minimum gap between obstacles

        # add title and instructions to the game
        self.title = TitleLabel()
        self.add_widget(self.title)

        Window.bind(on_key_down=self.key_down)

        Clock.schedule_interval(self.update, 1.0 / 60.0)  # call the update function 60 times per second
        self.game_started = False  # initialize the game_started flag to False

    def key_down(self, window, key, *args):
        if key == 32:  # space key
            self.remove_widget(self.title)
            # self.player.start_game()
            self.game_started = True
        elif key == 273 and self.game_started:  # up key
            self.player.dy = upward_movement  # move the helicopter up when the up key is pressed

    def update(self, dt):
        if self.game_started:
            self.player.dy += gravity  # apply gravity to the helicopter
            self.player.move_helicopter()  # move the helicopter

            # generate obstacles
            if random.random() < 0.01:
                obstacle_gap = random.randint(self.min_gap, self.height - self.min_gap)
                obstacle = Obstacle(gap=obstacle_gap)
                self.add_widget(obstacle)
                self.obstacles.append(obstacle)

            # move obstacles
            for obstacle in self.obstacles:
                obstacle.move_obstacle()
                if obstacle.x < -obstacle.width:
                    self.remove_widget(obstacle)
                    self.obstacles.remove(obstacle)
