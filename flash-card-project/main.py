from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

#---------------read text---------------------#
try:
    data = pd.read_csv("data/english-hungary-dictionary.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/en-hu-dict.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(up_title, text="English")
    canvas.itemconfig(down_title, text=current_card["English"])


#-------------------GUI-----------------------#
windows = Tk()
windows.title("EN-HU flash card")
windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_img = PhotoImage(file="images/card_front.png")
card_new_img = PhotoImage(file="images/card_back.png")
first_canvas_img = canvas.create_image(400, 263, image=card_img)
canvas.itemconfig(first_canvas_img, image=card_new_img)
canvas.grid(column=0, row=0, columnspan=2)

up_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
down_title = canvas.create_text(400, 263, text="", font=("Ariel", 60, "italic"))

check_img = PhotoImage(file="images/right.png")
check_button = Button(image=check_img, highlightthickness=0, command=next_card)
check_button.grid(column=1, row=1)

x_img = PhotoImage(file="images/wrong.png")
x_button = Button(image=x_img, highlightthickness=0, command=next_card)
x_button.grid(column=0, row=1)

next_card()

windows.mainloop()
