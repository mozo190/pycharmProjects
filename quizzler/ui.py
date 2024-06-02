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
        self.wrong_button = Button(image=self.wrong_image, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(row=2, column=0, pady=20)

        self.right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.right_image, highlightthickness=0, command=self.true_pressed)
        self.right_button.grid(row=2, column=1, pady=20)

        self.next_card()

        self.window.mainloop()

    def next_card(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.card_title, text=q_text)

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_card)


