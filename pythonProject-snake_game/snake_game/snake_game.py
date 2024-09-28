from kivy.clock import Clock
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

        # add food
        self.food = Food()
        self.add_widget(self.food)

        #initial direction of the snake
        self.direction = 'right'

        #creating clock event to move the snake
        Clock.schedule_interval(self.update, 1.0 / 10.0)

        Window.bind(on_key_down=self.on_key_down)

    def on_key_down(self, window, keyboard, key, text, modifiers):
        if key == 273:  # up
            self.direction = 'up'
        elif key == 274:  # down
            self.direction = 'down'
        elif key == 275:  # right
            self.direction = 'right'
        elif key == 276:  # left arrow key
            self.direction = 'left'
        return True

    def update(self, dt):
        # get current position of the snake's head
        x, y = self.snake.snake.pos
        if self.direction == 'up':
            y += 20
        elif self.direction == 'down':
            y -= 20
        elif self.direction == 'right':
            x += 20
        elif self.direction == 'left':
            x -= 20
        self.snake.snake.pos = x, y
        # self.snake.move(self.direction)
        # self.snake.check_collision(self.food)
        # self.snake.check_boundaries()
        # self.snake.check_self_collision()