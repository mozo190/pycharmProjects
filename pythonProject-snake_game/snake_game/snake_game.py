import random

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image
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

        self.game_over = False
        self.init_game()

        # initial direction of the snake
        self.direction = 'right'

        # creating clock event to move the snake
        Clock.schedule_interval(self.update, 1.0 / 10.0)

        Window.bind(on_key_down=self.on_key_down)

    def init_game(self):
        # add the snake to the game
        self.snake = Snake()
        self.add_widget(self.snake)

        # add food
        self.food = Food()
        self.add_widget(self.food)

    def on_key_down(self, instance, keyboard, key, text, modifiers):
        if key == 82:
            self.direction = 'up'
        elif key == 81:
            self.direction = 'down'
        elif key == 79:
            self.direction = 'right'
        elif key == 80:
            self.direction = 'left'
        # print(f"key pressed: {key}")

    def update(self, dt):
        x, y = self.snake.snake[0].pos
        if self.direction == 'up':
            y += 10
        elif self.direction == 'down':
            y -= 10
        elif self.direction == 'right':
            x += 10
        elif self.direction == 'left':
            x -= 10

        prev_position = [(segment.pos[0], segment.pos[1]) for segment in
                         self.snake.snake]  # save the previous position of the snake

        self.snake.snake[0].pos = x, y

        for i in range(1, len(self.snake.snake)):
            self.snake.snake[i].pos = prev_position[i - 1]

        # check if snake eats the food
        if self.check_collision(self.snake.snake[0], self.food.food):
            print("Eating the food")
            self.grow_snake(prev_position[-1])
            self.spawn_food()

    def check_collision(self, snake, food):
        return snake.collide_widget(food)

    def grow_snake(self, position):
        # add new snake to the body
        new_snake = Image(source='assets/img/snake_.png', size_hint=(None, None), size=(30, 30), pos=position)
        self.snake.snake.append(new_snake)
        self.add_widget(new_snake)

    def spawn_food(self):
        # spawn food at random position
        food_x = random.randint(0, (SCREEN_WIDTH - 30) // 20) * 20
        food_y = random.randint(0, (SCREEN_HEIGHT - 30) // 20) * 20
        self.food.food.pos = food_x, food_y
