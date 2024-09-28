import random

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.widget import Widget

from helicopterGame.helicopter import Helicopter, upward_movement, gravity
from helicopterGame.instructions_label import InstructionsLabel
from helicopterGame.obstacle import Obstacle
from helicopterGame.title_label import TitleLabel


class HelicopterGame(Widget):
    def __init__(self, **kwargs):
        super(HelicopterGame, self).__init__(**kwargs)

        self.game_over_label = None
        self.player = Helicopter()
        self.add_widget(self.player)
        self.obstacles = []  # list to store obstacles widgets
        self.min_gap = self.player.height * 4  # minimum gap between obstacles

        # add title and instructions to the game
        self.title = TitleLabel()
        self.add_widget(self.title)

        Window.bind(on_key_down=self.key_down)

        Clock.schedule_interval(self.update, 1.0 / 60.0)  # call the update function 60 times per second
        self.game_started = False  # initialize the game_started flag to False

    def key_down(self, window, key, *args):
        if key == 32:  # space key
            if not self.game_started:
                if self.game_over_label:
                    self.remove_widget(self.game_over_label)
                    self.game_over_label = None
                self.remove_widget(self.title) # remove the title and instructions
                self.game_started = True
        elif key == 273 and self.game_started:  # up key
            self.player.dy = upward_movement  # move the helicopter up when the up key is pressed

    def update(self, dt):
        if self.game_started:
            self.player.dy += gravity  # apply gravity to the helicopter
            self.player.move_helicopter()  # move the helicopter

            # generate obstacles
            if random.random() < 0.02:
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
                if self.check_collision(obstacle):
                    self.restart_game()


    def check_collision(self, obstacle):
        # check if the player has collided with the top part of the obstacle
        if (self.player.x < obstacle.x + obstacle.width and
                self.player.x + self.player.width > obstacle.x and
                self.player.y < obstacle.y_top + obstacle.height_top and
                self.player.y + self.player.height > obstacle.y_top):
            return True
        # check if the player has collided with the bottom part of the obstacle
        if (self.player.x < obstacle.x + obstacle.width and
                self.player.x + self.player.width > obstacle.x and
                self.player.y < obstacle.y_bottom + obstacle.height_bottom and
                self.player.y + self.player.height > obstacle.y_bottom):
            return True
        return False

    def restart_game(self):
        # reset the player's position and speed
        self.player.reset_position()
        # remove all obstacles
        for obstacle in self.obstacles:
            self.remove_widget(obstacle)
        self.obstacles.clear()

        # reset game state
        self.game_started = False
        # add title and instructions
        self.game_over_label = InstructionsLabel()
        self.add_widget(self.game_over_label)

