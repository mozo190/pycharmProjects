from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class UI:
    def __init__(self, quiz_brain: "QuizBrain"):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Flash Card")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Ariel", 10, "bold"))
        self.score_label.grid(row=0, column=1, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.card_title = self.canvas.create_text(150, 125, text="Title", font=("Ariel", 20, "italic"),
                                                  fill=THEME_COLOR,
                                                  width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_image, highlightthickness=0, command=self.next_card)
        self.wrong_button.grid(row=2, column=0, pady=20)

        self.right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.right_image, highlightthickness=0, command=self.next_card)
        self.right_button.grid(row=2, column=1, pady=20)

        self.next_card()

        self.window.mainloop()

    def next_card(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.card_title, text=q_text)
