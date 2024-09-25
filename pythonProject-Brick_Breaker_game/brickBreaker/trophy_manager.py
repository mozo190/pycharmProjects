from kivy.uix.image import Image


class TrophyManager:
    def __init__(self, num_trophies, widget):
        self.num_trophies = num_trophies
        self.trophies = []
        self.widget = widget  # the widget to add the trophies to
        self.initialize_trophies()

    def initialize_trophies(self):
        for i in range(self.num_trophies):
            trophy = Image(source='assets/img/Golden-champion-cup-black-white.png')
            trophy.size = 50, 50
            trophy.pos = 10 + i * 50, self.widget.height - 50
            self.trophies.append(trophy)
            self.widget.add_widget(trophy)

    def update_trophies(self, level):
        if level < self.num_trophies:
            # remove the old trophy
            self.widget.remove_widget(self.trophies[level])
            # create and add the new trophy
            trophy = Image(source='assets/img/Golden-champion-cup.png')
            trophy.size = 50, 50
            trophy.pos = 10 + level * 50, self.widget.height - 50
            self.trophies[level] = trophy
            self.widget.add_widget(trophy)
