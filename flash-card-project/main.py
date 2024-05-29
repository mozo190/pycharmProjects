from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

#-------------------GUI-----------------------#
windows = Tk()
windows.title("EN-HU flash card")
windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_img)
canvas.grid(column=0, row=0)

windows.mainloop()
