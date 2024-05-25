from tkinter import *

FONT = ("Arial", 12, "normal")

window = Tk()
window.title("Mile to km converter")
window.minsize(width=300, height=150)
window.config(padx=25, pady=25)

input_box = Entry(width=15)
input_box.get()
input_box.grid(column=1, row=0)

label1 = Label(text="Mile", font=FONT)
label1.grid(column=2, row=0)

label2 = Label(text="is equal to", font=FONT)
label2.grid(column=0, row=1)

label3 = Label(text=0, font=FONT)
label3.grid(column=1, row=1)

label4 = Label(text="Km", font=FONT)
label4.grid(column=2, row=1)


def button_clicked():
    new_text = int(input_box.get()) * 1.7
    label3.config(text=new_text)


button1 = Button(text="Calculate", command=button_clicked)
button1.grid(column=1, row=2)

window.mainloop()
