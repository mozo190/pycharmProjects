from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Kenya quotes App")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kenya quotes", width=250, font=("Arial", 20, "bold"), fill="black")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0)
kanye_button.grid(row=1, column=0)

window.mainloop()