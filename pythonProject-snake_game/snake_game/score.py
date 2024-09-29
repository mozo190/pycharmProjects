from kivy.uix.label import Label


class Score(Label):
    def __init__(self, **kwargs):
        super(Score, self).__init__(**kwargs)
        # self.score_of_number = 0
        self.font_size = 30
        self.color = (0, 0, 0, 1)  # black color

        # initial score text
        self.size_hint = (None, None)
        self.pos = (20, 400)
        self.text = "Score: 0"
        self.size = (self.font_size * len(self.text), self.font_size)

    # def update_score(self):
    #     self.score_of_number += 1  # increment the score
    #     self.text = "Score: " + str(self.score_of_number)  # update the score text
    #     self.size = (self.font_size * len(self.text), self.font_size)
