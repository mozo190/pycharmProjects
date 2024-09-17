from random import randint

from kivy.app import App
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.widget import Widget

# set the window size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 1.0 / 60.0
ENEMY_SPEED = 1

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

    score = 0  # initialize the score to 0
    score_label = ObjectProperty(None)  # create a score label

    def __init__(self, **kwargs):
        super(SpaceInvadersGame, self).__init__(**kwargs)
        self.quit_button = None
        self.again_button = None
        self.button_layout = None
        with self.canvas:
            Color(0, 0, 0, 1)
            self.rect = Rectangle(size=(SCREEN_WIDTH, SCREEN_HEIGHT), pos=(0, 0))

        # label to display the score
        self.score_label = Label(text='SCORE: 0', pos=(10, SCREEN_HEIGHT - 40), size_hint=(None, None),
                                 font_size=20, size=(100, 40))  # create a label to display the score
        self.score_label.color = (1, 1, 1, 1)  # set the color of the label to white
        self.add_widget(self.score_label)

        # add sound to the game
        self.game_over_sound = SoundLoader.load('static/assets/audio/game-over-01.wav')
        self.game_over_sound.volume = 1.5
        self.shooting_sound = SoundLoader.load('static/assets/audio/shooting_sounds_017.wav')
        self.shooting_sound.volume = 0.5

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

        self.enemy_speed = ENEMY_SPEED  # initial speed of the enemies
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
        self.shooting_sound.play()

    def spawn_enemies(self, dt):
        if self.game_over_flag:  # do not spawn enemies if the game is over
            return
        # ensure no fewer than 10 enemies on the screen
        while len(self.enemies) < 10:
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

                    self.score += 1  # increment the score
                    self.score_label.text = f'SCORE: {self.score}'  # update the score label
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

        # play the game over sound
        if self.game_over_sound:
            self.game_over_sound.play()

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
        self.game_over_image.size_hint = (None, None)
        self.add_widget(self.game_over_image)
        self.children.append(self.game_over_image)  # add the game over image to the children list

        # create a BoxLayout to hold the play again and quit button
        self.button_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(150, 50),
                                       pos=(SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 - 150))

        # create the play again button
        self.again_button = Button(text='Again', on_press=self.again_button_pressed)

        # create the quit button
        self.quit_button = Button(text="Quit",
                                  on_press=self.quit_button_pressed)  # bind the button to the quit_button_pressed()

        # add the buttons to the button layout
        self.button_layout.add_widget(self.again_button)
        self.button_layout.add_widget(self.quit_button)

        # add the button layout to the screen
        self.add_widget(self.button_layout)
        self.children.append(self.button_layout)  # add the button layout to the children list

    def again_button_pressed(self, instance):

        # remove the game over image and button layout
        self.remove_widget(self.game_over_image)
        self.remove_widget(self.button_layout)
        # reset the game
        self.game_over_flag = False
        self.spaceship.pos = (SCREEN_WIDTH / 2 - self.spaceship.width / 2, 20)
        self.add_enemies()

    def quit_button_pressed(self, instance):
        App.get_running_app().stop()  # stop the app


class SpaceInvadersApp(App):
    def build(self):
        return SpaceInvadersGame()


if __name__ == '__main__':
    SpaceInvadersApp().run()
