from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import BooleanProperty
from kivy.uix.widget import Widget
from kivy.utils import platform
from plyer import accelerometer

from .background import Background
from .ball import Ball
from .bat import Bat
from .brick import Brick
from .game_over import GameOver
from .game_win import GameWin
from .play_button import PlayButton
from .trophy_manager import TrophyManager


class BrickBreakerGame(Widget):
    game_over_flag = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(BrickBreakerGame, self).__init__(**kwargs)

        # add background image
        self.play_button = None
        self.background = Background()
        self.add_widget(self.background)

        # add ball
        self.ball = Ball()
        self.add_widget(self.ball)

        # add bat
        self.bat = Bat()
        self.add_widget(self.bat)

        # add bricks
        self.bricks = Brick()
        self.add_widget(self.bricks)

        self.game_over = GameOver()
        self.add_widget(self.game_over)

        self.game_win = GameWin()
        self.add_widget(self.game_win)

        self.current_level = 0  # initialize the current level to 0
        self.trophy_manager = TrophyManager(num_trophies=5, widget=self)  # create a trophy manager
        self.initialize_level()

        Window.bind(on_key_down=self.on_key_down)
        Window.bind(on_key_up=self.on_key_up)

        # add touch events
        Window.bind(on_touch_down=self.on_touch_down)

        # add accelerometer and enable only on android
        if platform == 'android':
            accelerometer.enable()
            Clock.schedule_interval(self.update_accel, 1.0 / 30.0)

        # schedule the update function
        Clock.schedule_interval(self.update, 1.0 / 60.0)
        Clock.schedule_once(self.ball.speed_up_ball, 30)

    def initialize_level(self):
        # initialize the level
        level_data = [
            (3, 7),
            (4, 8),
            (5, 9),
            (6, 10),
            (7, 11)
        ]
        if self.current_level < len(level_data):
            rows, cols = level_data[self.current_level]
            self.bricks.initialize_bricks(rows, cols)
        else:
            self.game_win.drawImage()

    def on_key_down(self, window, key, scancode, codepoint, modifier, *args):
        if key == 276:  # left arrow key
            self.bat.move_left()
        elif key == 275:  # right arrow key
            self.bat.move_right()

    def on_key_up(self, window, key, *args):
        pass

    def on_touch_down(self, touch, *args):
        if touch.x < self.width / 2:
            self.bat.move_left()
        else:
            self.bat.move_right()

    def update_accel(self, dt):
        accel = accelerometer.acceleration
        if accel:
            x, y, z = accel
            self.update_bat_position(x)

    def update_bat_position(self, accel_x):
        if accel_x < -0.1:
            self.bat.move_left()
        elif accel_x > 0.1:
            self.bat.move_right()

    def update(self, dt):
        if self.game_over_flag:
            return  # do not update the game if it is over

        self.ball.move_ball()
        # check for collision of ball with walls
        if self.ball.ball_x < 0 or self.ball.ball_x > self.width - self.ball.WIDTH:
            self.ball.ball_vel_x *= -1
            self.ball.ball_sound.play()

        if self.ball.ball_y > self.height - self.ball.HEIGHT:
            self.ball.ball_vel_y *= -1
            self.ball.ball_sound.play()

        if self.ball.ball_y < 0:
            self.ball.ball_vel_y *= -1
            self.ball.ball_sound.play()

        if self.ball.ball_y < 0:
            self.end_game()

        # self.check_collision()
        if self.check_collision(self.ball.ballImage, self.bat.batImage):
            self.ball.ball_vel_y *= -1
            self.ball.ball_sound.play()  # play the sound of ball hitting the bat

        # check the collision fo bat with left and right walls
        if self.bat.bat_x < 0:
            self.bat.bat_x = 0
        elif self.bat.bat_x > self.width - self.bat.WIDTH:
            self.bat.bat_x = self.width - self.bat.WIDTH  # set the bat to the right wall

        # check for collision of ball with bricks
        bricks_to_remove = []

        for brick in self.bricks.brick_list:
            if self.check_collision(self.ball.ballImage, brick):
                self.ball.ball_vel_y *= -1
                self.ball.ball_sound.play()  # play the sound of ball hitting the brick
                brick.pos = 1000, 1000
                bricks_to_remove.append(brick)
                self.bricks.no_of_bricks -= 1

        for brick in bricks_to_remove:
            self.bricks.brick_list.remove(brick)
            self.remove_widget(brick)
        if self.bricks.no_of_bricks == 0:
            self.win_game()

    def check_collision(self, ball, bat):
        return (ball.x < bat.right and
                ball.right > bat.x and
                ball.y < bat.top and
                ball.top > bat.y)

    def end_game(self):
        self.game_over_flag = True
        self.ball.ball_vel_x = 0
        self.ball.ball_vel_y = 0
        self.game_over.drawImage()
        self.background.stop_music()
        self.add_play_button()
        if platform == 'android':
            accelerometer.disable()

    def win_game(self):

        self.ball.ball_vel_x = 0
        self.ball.ball_vel_y = 0
        self.trophy_manager.update_trophies(self.current_level)  # update the trophy
        self.current_level += 1  # increment the current level

        level_data = [
            (3, 7),
            (4, 8),
            (5, 9),
            (6, 10),
            (7, 11)
        ]

        if self.current_level < len(level_data):
            rows, cols = level_data[self.current_level]
            self.bricks.initialize_bricks(rows, cols)  # initialize the bricks for the next level

            # ball reposition
            self.ball.ball_x = self.width / 2
            self.ball.ball_y = self.height / 2
            self.ball.ball_vel_x = 4  # reset the ball velocity
            self.ball.ball_vel_y = 4
            self.ball.update_position()  # reset the ball
        else:
            self.game_win.drawImage()
            self.game_over_flag = True
        self.background.stop_music()
        self.add_play_button()
        if platform == 'android':
            accelerometer.disable()

        if not self.game_over_flag:
            self.background.play_music()

    def add_play_button(self):
        self.play_button = PlayButton()  # create a play button
        self.play_button.bind(on_press=self.restart_game)  # bind the start_game function to the play button
        self.add_widget(self.play_button)  # add the play button to the screen

    def restart_game(self):
        self.remove_widget(self.play_button)  # remove the play button
        self.game_over_flag = False  # reset the game over flag
        self.ball.update_position()  # reset the ball position
        self.bat.update_position()  # reset the bat position
        self.bricks.initialize_bricks(3, 7)  # initialize the bricks for the first level
        self.ball.ball_vel_x = 2  # reset the ball velocity
        self.ball.ball_vel_y = 2  # reset the ball velocity
        self.background.play_music()  # play the background music
        if platform == 'android':
            accelerometer.enable()
            Clock.schedule_interval(self.update_accel, 1.0 / 30.0)
