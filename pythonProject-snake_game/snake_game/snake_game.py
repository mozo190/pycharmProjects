from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget

from snake_game.config import SCREEN_HEIGHT, SCREEN_WIDTH
from snake_game.food import Food
from snake_game.snake import Snake

Window.size = (SCREEN_WIDTH, SCREEN_HEIGHT)


class SnakeGame(Widget):
    def __init__(self, **kwargs):
        super(SnakeGame, self).__init__(**kwargs)

        with self.canvas:
            Color(1, 1, 0.5, 0.9)  # add color background
            Rectangle(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

        self.snake = Snake()
        # self.snake.start()
        self.add_widget(self.snake)
        # Clock.schedule_interval(self.snake.move, 1.0 / 10.0)

        # add food
        self.food = Food()
        self.add_widget(self.food)

        Window.bind(on_key_down=self.on_key_down)

    def on_key_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 273:  # up
            self.snake.move_up()
        elif keycode == 274:  # down
            self.snake.move_down()
        elif keycode == 275:  # right
            self.snake.move_right()
        elif keycode == 276:  # left key
            self.snake.move_left()
        else:
            pass
        return True
