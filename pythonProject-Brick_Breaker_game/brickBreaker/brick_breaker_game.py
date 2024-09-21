from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import BooleanProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget

from .ball import Ball
from .bat import Bat
from .brick import Brick


class GameOver(Widget):
    def __init__(self, **kwargs):
        super(GameOver, self).__init__(**kwargs)
        self.WIDTH = 800
        self.HEIGHT = 600
        self.gox = 30
        self.goy = 150

        self.goImage = Image(source='assets/img/gameover.png')
        self.goImage.size = self.WIDTH, self.HEIGHT
        self.goImage.pos = self.gox, self.goy
        self.add_widget(self.goImage)
        self.goImage.opacity = 0  # Initialize invisible

    def drawImage(self):
        self.goImage.opacity = 1  # visible


class BrickBreakerGame(Widget):
    game_over_flag = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(BrickBreakerGame, self).__init__(**kwargs)

        # add background image
        self.background = Image(source='assets/img/bk.bmp')
        self.background.allow_stretch = True
        self.background.keep_ratio = False
        self.background.size = 800, 600
        self.background.pos = 0, 0
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
        self.bricks.initialize_bricks()

        self.game_over = GameOver()
        self.add_widget(self.game_over)

        Window.bind(on_key_down=self.on_key_down)
        Window.bind(on_key_up=self.on_key_up)
        # schedule the update function
        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def on_key_down(self, window, key, scancode, codepoint, modifier, *args):
        if key == 276:  # left arrow key
            self.bat.move_left()
        elif key == 275:  # right arrow key
            self.bat.move_right()

    def on_key_up(self, window, key, *args):
        pass

    def update(self, dt):
        if self.game_over_flag:
            return  # do not update the game if it is over

        self.ball.move_ball()
        # check for collision of ball with walls
        if self.ball.ball_x < 0 or self.ball.ball_x > self.width - self.ball.WIDTH:
            self.ball.ball_vel_x *= -1

        if self.ball.ball_y > self.height - self.ball.HEIGHT:
            self.ball.ball_vel_y *= -1

        if self.ball.ball_y < 0:
            self.ball.ball_vel_y *= -1

        if self.ball.ball_y < 0:
            self.end_game()

        # self.check_collision()
        if self.check_collision(self.ball.ballImage, self.bat.batImage):
            self.ball.ball_vel_y *= -1

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
                brick.pos = 1000, 1000
                bricks_to_remove.append(brick)

        for brick in bricks_to_remove:
            self.bricks.brick_list.remove(brick)
            self.remove_widget(brick)

    def check_collision(self, ball, bat):
        return (ball.x < bat.right and
                ball.right > bat.x and
                ball.y < bat.top and
                ball.top > bat.y)

    def end_game(self):
        self.game_over_flag = True
        self.ball.ball_vel_x = 0
        self.ball.ball_vel_y = 0
        # self.remove_widget(self.ball)
        # self.remove_widget(self.bat)
        # self.remove_widget(self.bricks)
        # self.add_widget(Image(source='assets/img/game_over.bmp'))
        # Clock.unschedule(self.update)
        # Window.unbind(on_key_down=self.on_key_down)
        # Window.unbind(on_key_up=self.on_key_up)
        # Window.close()
