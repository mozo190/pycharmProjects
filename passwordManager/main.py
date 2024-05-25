from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=250, height=300, highlightthickness=5, highlightcolor="black")
lock_img = PhotoImage(file="logo.png")
canvas.create_image(125, 140, image=lock_img)
canvas.pack()

window.mainloop()