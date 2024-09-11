import random
import time

from kivy.app import App
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 250
DINO_Y_POS = 30
GRAVITY = -1.2
JUMP_VELOCITY = 6
GROUND_SPEED = 4
PTERA_SPEED = 5
PTERA_FLAP_INTERVAL = 0.2
MIN_CACTUS_GAP = 200
MAX_CACTUS_GAP = 400
FPS = 1 / 60

Window.size = (SCREEN_WIDTH, SCREEN_HEIGHT)
Window.clearcolor = (1, 1, 1, 1)


class Ground(Image):
    def __init__(self, **kwargs):
        super(Ground, self).__init__(**kwargs)
        self.ground_length = 1202
        self.image1 = Image(source='static/assets/img/sprites/ground.png', pos=(0, 0))
        self.image1.size = (self.ground_length, 26)

        self.image2 = Image(source='static/assets/img/sprites/ground.png', pos=(self.ground_length, 0))
        self.image2.size = (self.ground_length, 26)

        self.add_widget(self.image1)
        self.add_widget(self.image2)

    def update(self, dt):
        self.image1.x -= GROUND_SPEED
        self.image2.x -= GROUND_SPEED

        if self.image1.x + self.ground_length <= 0:
            self.image1.x = self.image2.x + self.ground_length
        elif self.image2.x + self.ground_length <= 0:
            self.image2.x = self.image1.x + self.ground_length

    def reset(self):
        self.image1.pos = 0, 0
        self.image2.pos = self.ground_length, 0


class Dino(Image):
    g = GRAVITY
    up = JUMP_VELOCITY  # INITIAL VELOCITY
    t = 0
    jumping = False

    def __init__(self, **kwargs):
        super(Dino, self).__init__(**kwargs)
        self.source = 'static/assets/img/sprites/dino_.png'
        self.width, self.height = (44, 48)
        self.size = (self.width, self.height)
        self.pos = (20, DINO_Y_POS)
        self.step_images = ['static/assets/img/sprites/dino_.png',
                            'static/assets/img/sprites/dino_1.png',
                            'static/assets/img/sprites/dino_2.png']
        self.step_index = 0

        Clock.schedule_interval(self.step, 0.1)

    def step(self, dt):
        self.step_index = (self.step_index + 1) % 3
        self.source = self.step_images[self.step_index]

    def jump(self):
        if not self.jumping:
            self.jumping = True
            self.up = JUMP_VELOCITY
            self.t = 0

    def update(self, dt):
        if self.jumping:
            self.up += self.g * self.t  # v = u + at
            self.y += self.up
            self.t += dt

            if self.y <= DINO_Y_POS:
                self.y = DINO_Y_POS
                self.jumping = False
                self.t = 0
                self.up = JUMP_VELOCITY


class Cactus(Image):
    def __init__(self, **kwargs):
        super(Cactus, self).__init__(**kwargs)
        cactus_type = random.choice(['static/assets/img/sprites/cacti-big.png',
                                     'static/assets/img/sprites/cacti-small.png'])
        self.source = cactus_type
        if cactus_type == 'static/assets/img/sprites/cacti-big.png':
            self.size = (65, 45)
        else:
            self.size = (45, 44)
        self.pos = (SCREEN_WIDTH, DINO_Y_POS)
        self.speed = GROUND_SPEED

    def update(self, dt):
        self.x -= self.speed
        self.pos = (self.x, self.y)
        if self.x <= -self.width:
            self.parent.remove_widget(self)
        self.pos = (self.x, self.y)


class Ptera(Image):
    def __init__(self, **kwargs):
        super(Ptera, self).__init__(**kwargs)
        self.altitude = random.choice([175, 150, 110, 30])
        self.size = (46, 40)
        self.pos = (random.randint(750, 1000), self.altitude)
        self.speed = PTERA_SPEED
        self.source = 'static/assets/img/sprites/ptera1.png'
        self.flap_images = ['static/assets/img/sprites/ptera1.png',
                            'static/assets/img/sprites/ptera2.png']
        self.flap_index = 0

        Clock.schedule_interval(self.flap, PTERA_FLAP_INTERVAL)

    def flap(self, dt):
        self.flap_index = (self.flap_index + 1) % 2
        self.source = self.flap_images[self.flap_index]

    def update(self, dt):
        self.x -= self.speed
        self.pos = (self.x, self.y)
        if self.x <= -self.width:
            self.parent.remove_widget(self)


class Cloud(Image):
    def __init__(self, **kwargs):
        super(Cloud, self).__init__(**kwargs)
        self.source = 'static/assets/img/sprites/cloud.png'
        self.WIDTH, self.HEIGHT = (70, 40)
        self.size = (self.WIDTH, self.HEIGHT)
        self.speed = random.randint(1, 4)
        self.reset()

    def reset(self):
        self.pos = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 100), random.randint(70, 210)

    def update(self, dt):
        self.x -= self.speed
        if self.x <= -self.WIDTH:
            self.reset()
        self.pos = (self.x, self.y)


class DinoGame(Widget):
    def __init__(self, **kwargs):
        super(DinoGame, self).__init__(**kwargs)

        self.ground = Ground()
        self.add_widget(self.ground)

        self.jump_sound = SoundLoader.load('static/assets/sounds/jump.wav')
        self.hit_sound = SoundLoader.load('static/assets/sounds/hit.wav')
        self.background_music = SoundLoader.load('static/assets/sounds/background.mp3')

        if self.background_music:
            self.background_music.loop = True
            self.background_music.play()

        self.obstacles = []
        self.obstacle_start = time.time()
        self.minimum_time = 1.5

        self.clouds = [Cloud() for _ in range(3)]  # create 3 clouds
        for cloud in self.clouds:
            self.add_widget(cloud)

        self.dino = Dino()  # Image(source='dino.png', pos=(100, 0))
        self.add_widget(self.dino)

        self.game_over_image = Image(source='static/assets/img/sprites/game_over.png')
        self.game_over_image.size_hint = (None, None)
        self.game_over_image.size = (190, 11)
        self.game_over_image.pos = (SCREEN_WIDTH // 2 - 95, SCREEN_HEIGHT // 2 + 50)

        self.replay_button_image = Button(background_normal='static/assets/img/sprites/replay_button.png')
        self.replay_button_image.size_hint = (None, None)
        self.replay_button_image.size = (50, 50)
        self.replay_button_image.pos = (SCREEN_WIDTH // 2 - 35, SCREEN_HEIGHT // 2 - 50)
        self.replay_button_image.bind(on_press=self.reset_game)

        self.game_over = False

        Clock.schedule_interval(self.update, FPS)  # update at 60Hz
        Window.bind(on_key_down=self.on_key_down)  # bind the key down event

    def on_key_down(self, window, key, *args):
        if key == 32:  # space key
            if self.jump_sound:
                self.jump_sound.play()
            if self.game_over:
                self.reset_game()
            else:
                self.dino.jump()

    def update(self, dt):
        if self.game_over:
            return

        self.dino.update(dt)
        self.ground.update(dt)

        for cactus in self.obstacles:
            cactus.update(dt)

        if len(self.obstacles) < 2:
            self.spawn_obstacle()

        # clean up obstacles that have moved off the screen
        self.obstacles = [cactus for cactus in self.obstacles if cactus.x > -cactus.width]

        for cloud in self.clouds:
            cloud.update(dt)

        self.check_collision()

    def spawn_obstacle(self):
        if random.random() < 0.8:  # 80% chance a cactus will appear
            self.spawn_cactus()
        else:
            self.spawn_ptera()

    def spawn_cactus(self):
        if self.obstacles:
            last_cactus = self.obstacles[-1]
            new_cactus_x = last_cactus.x + last_cactus.width + random.randint(MIN_CACTUS_GAP, MAX_CACTUS_GAP)
        else:
            new_cactus_x = SCREEN_WIDTH + random.randint(MIN_CACTUS_GAP, MAX_CACTUS_GAP)

        new_cactus = Cactus()
        new_cactus.pos = (new_cactus_x, DINO_Y_POS)
        self.obstacles.append(new_cactus)
        self.add_widget(new_cactus)

    def spawn_ptera(self):
        new_ptera = Ptera()
        self.obstacles.append(new_ptera)
        self.add_widget(new_ptera)

    def check_collision(self):
        # if self.hit_sound:

        for obstacle in self.obstacles:

            if self.dino.collide_widget(obstacle):
                self.hit_sound.play()
                self.end_game()

    def end_game(self):
        if self.game_over:
            return  # game is already over

        self.game_over = True
        self.add_widget(self.game_over_image)
        self.add_widget(self.replay_button_image)
        self.replay_button_image.unbind(on_press=self.reset_game)  # unbind the reset_game method from the button
        self.replay_button_image.bind(on_press=self.reset_game)  # bind the reset_game method to the button

    def reset_game(self, *args):
        self.game_over = False
        self.remove_widget(self.game_over_image)
        self.remove_widget(self.replay_button_image)

        # reset the dinosaur position and velocity to the initial values
        self.dino.y = DINO_Y_POS
        self.dino.jumping = False
        self.dino.t = 0
        self.dino.up = JUMP_VELOCITY
        self.dino.x = 20

        # remove all the obstacles from the screen
        for obstacle in self.obstacles:
            self.remove_widget(obstacle)
        self.obstacles = []

        # reset ground and clouds
        self.ground.reset()
        for cloud in self.clouds:
            cloud.reset()


class DinoApp(App):
    def build(self):
        return DinoGame()


if __name__ == '__main__':
    DinoApp().run()
