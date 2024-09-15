from random import randint

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.properties import ListProperty
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


def is_collision(bullet, enemy):
    if (bullet.x < enemy.right and bullet.right > enemy.x and
            bullet.y < enemy.top and bullet.top > enemy.y):
        return True
    return False


class SpaceInvadersGame(Widget):
    bullets = ListProperty([])
    enemies = ListProperty([])

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

        Clock.schedule_interval(self.update, FPS)
        Clock.schedule_interval(self.spawn_enemies, 1.0 / 2.0)

        self.add_enemies()

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
            enemy.y -= 4
            if enemy.top < 0:
                self.remove_widget(enemy)
                self.enemies.remove(enemy)

        self.check_collision()

    def fire_bullet(self):
        bullet = Bullet()
        bullet.size = (2, 10)
        bullet.pos = (self.spaceship.center_x - bullet.width / 2, self.spaceship.top)  # set the bullet position
        self.add_widget(bullet)
        self.bullets.append(bullet)

    def spawn_enemies(self, dt):
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
                if is_collision(bullet, enemy):
                    self.remove_widget(bullet)
                    self.bullets.remove(bullet)
                    self.remove_widget(enemy)
                    self.enemies.remove(enemy)


class SpaceInvadersApp(App):
    def build(self):
        return SpaceInvadersGame()


if __name__ == '__main__':
    SpaceInvadersApp().run()
