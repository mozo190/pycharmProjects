from random import randint

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget

# set the window size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 1.0 / 60.0

Window.size = (SCREEN_WIDTH, SCREEN_HEIGHT)


class Bullet(Widget):
    def __init__(self, **kwargs):
        super(Bullet, self).__init__(**kwargs)
        with self.canvas:
            Color(1, 0, 0, 1)
            self.rect = Rectangle(size=(2, 10), pos=self.pos)

        self.bind(pos=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos


class Enemy(Image):
    def __init__(self, **kwargs):
        super(Enemy, self).__init__(**kwargs)
        self.source = 'static/assets/img/enemies.png'
        self.size_hint = (None, None)
        self.size = (50, 50)
        self.pos = (0, 0)


class SpaceInvadersGame(Widget):
    bullets = ListProperty([])
    enemies = ListProperty([])
    game_over_flag = False
    game_over_image = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(SpaceInvadersGame, self).__init__(**kwargs)
        with self.canvas:
            Color(0, 0, 0, 1)
            self.rect = Rectangle(size=(SCREEN_WIDTH, SCREEN_HEIGHT), pos=(0, 0))

        # Add the spaceship image
        # self.spaceship = Image(source='static/assets/img/spaceship.png', size=(74, 74),
        #                        pos=(SCREEN_WIDTH / 2 - 50, 20))
        self.spaceship = Image(source='static/assets/img/spaceship.png')
        self.spaceship.size_hint = (None, None)
        self.spaceship.size = (74, 74)
        self.spaceship.pos = (SCREEN_WIDTH / 2 - self.spaceship.width / 2, 20)
        self.add_widget(self.spaceship)

        # bind keyboard events
        Window.bind(on_key_down=self.on_key_down)
        Window.bind(on_key_up=self.on_key_up)

        self.left_pressed = False
        self.right_pressed = False

        self.enemy_speed = 2  # initial speed of the enemies
        Clock.schedule_interval(self.update, FPS)
        Clock.schedule_interval(self.spawn_enemies, 1.0 / 2.0)
        Clock.schedule_interval(self.increase_enemy_speed, 60)  # increase the enemy speed every 60 seconds

        self.add_enemies()

    def increase_enemy_speed(self, dt):
        self.enemy_speed += 1  # increase the enemy speed by 1

    def on_key_down(self, window, key, *args):
        if key == 276:  # left arrow key
            self.left_pressed = True
        elif key == 275:  # right arrow key
            self.right_pressed = True

        elif key == 32:  # space key
            self.fire_bullet()

    def on_key_up(self, window, key, *args):
        if key == 276:
            self.left_pressed = False
        elif key == 275:
            self.right_pressed = False

    def update(self, dt):
        if self.game_over_flag:
            return
        if self.left_pressed:
            self.spaceship.x -= 5  # move the spaceship to the left
            if self.spaceship.x < 0:
                self.spaceship.x = 0
        elif self.right_pressed:
            self.spaceship.x += 5  # move the spaceship to the right
            if self.spaceship.right > self.width:
                self.spaceship.right = self.width

        # update the bullets
        for bullet in self.bullets:
            bullet.y += 10
            if bullet.top > self.height:
                self.remove_widget(bullet)
                self.bullets.remove(bullet)

        # update the enemies
        for enemy in self.enemies:
            enemy.y -= self.enemy_speed  # dynamically change the speed of the enemies
            if enemy.top < 0:
                self.remove_widget(enemy)
                self.enemies.remove(enemy)

        self.check_collision()

    def fire_bullet(self):
        if self.game_over_flag:
            return
        bullet = Bullet()
        bullet.size = (2, 10)
        bullet.pos = (self.spaceship.center_x - bullet.width / 2, self.spaceship.top)  # set the bullet position
        self.add_widget(bullet)
        self.bullets.append(bullet)

    def spawn_enemies(self, dt):
        if self.game_over_flag:  # do not spawn enemies if the game is over
            return
        # ensure no fewer than 10 enemies on the screen
        while len(self.enemies) < 15:
            enemy = Enemy()
            enemy.pos = (randint(0, SCREEN_WIDTH - enemy.width), SCREEN_HEIGHT)
            self.add_widget(enemy)
            self.enemies.append(enemy)

    def add_enemies(self):
        for i in range(10):
            enemy = Enemy()
            enemy.pos = (randint(0, SCREEN_WIDTH - enemy.width), SCREEN_HEIGHT)
            self.add_widget(enemy)
            self.enemies.append(enemy)

    def check_collision(self):
        for bullet in self.bullets:
            for enemy in self.enemies:
                if self.is_collision(bullet, enemy):
                    self.remove_widget(bullet)
                    self.bullets.remove(bullet)
                    self.remove_widget(enemy)
                    self.enemies.remove(enemy)
                    break
        for enemy in self.enemies[:]:
            if self.is_collision(self.spaceship, enemy):
                self.game_over()

    def is_collision(self, bullet, enemy):
        if (bullet.x < enemy.right and bullet.right > enemy.x and
                bullet.y < enemy.top and bullet.top > enemy.y):
            return True
        return False

    def game_over(self):
        self.game_over_flag = True
        # remove all the bullets and enemies
        for bullet in self.bullets:
            self.remove_widget(bullet)
        for enemy in self.enemies:
            self.remove_widget(enemy)
        # clear the lists
        self.bullets.clear()
        self.enemies.clear()

        # add the game over image
        self.game_over_image = Image(source='static/assets/img/game_over.png', size=(600, 400),
                                     pos=(SCREEN_WIDTH / 2 - 300, SCREEN_HEIGHT / 2 - 200))
        self.add_widget(self.game_over_image)

        # create a BoxLayout to hold the play again and quit button
        button_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(200, 50),
                                  pos=(SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 - 100))

        # create the play again button
        again_button = Button(text='Play Again', on_press=self.again_button_pressed)
        again_button.bind(on_press=self.again_button_pressed)  # bind the button to the again_button_pressed method

        # create the quit button
        quit_button = Button(text="Quit",
                             on_press=self.quit_button_pressed)  # bind the button to the quit_button_pressed method
        quit_button.bind(on_press=self.quit_button_pressed)

        # add the buttons to the button layout
        button_layout.add_widget(again_button)
        button_layout.add_widget(quit_button)

        # add the button layout to the screen
        self.add_widget(button_layout)

    def again_button_pressed(self, instance):
        self.game_over_flag = False
        self.remove_widget(self.game_over_image)
        self.spaceship.pos = (SCREEN_WIDTH / 2 - self.spaceship.width / 2, 20)
        self.add_enemies()

    def quit_button_pressed(self, instance):
        App.get_running_app().stop()


class SpaceInvadersApp(App):
    def build(self):
        return SpaceInvadersGame()


if __name__ == '__main__':
    SpaceInvadersApp().run()
