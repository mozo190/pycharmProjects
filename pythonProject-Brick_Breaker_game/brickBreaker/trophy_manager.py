from kivy.uix.image import Image


class TrophyManager:
    def __init__(self, num_trophies, widget):
        self.num_trophies = num_trophies
        self.trophies = []
        self.widget = widget  # the widget to add the trophies to
        self.initialize_trophies()

    def initialize_trophies(self):
        for i in range(self.num_trophies):
            trophy = Image(source='assets/img/trophy_bl_w.png')
            trophy.size = 50, 50
            trophy.pos = 1 + i * 50, 600 - 55
            self.trophies.append(trophy)
            self.widget.add_widget(trophy)

    def update_trophies(self, level):
        if level < self.num_trophies:
            # remove the old trophy
            self.widget.remove_widget(self.trophies[level])
            # create and add the new trophy
            trophy = Image(source='assets/img/trophy.png')
            trophy.size = 50, 50
            trophy.pos = 1 + level * 50, 600 - 55
            self.trophies[level] = trophy
            self.widget.add_widget(trophy)
