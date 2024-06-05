from tkinter import *

FONT = ("Arial", 12, "normal")

window = Tk()
window.title("Miles to Kilometer Converter")
# window.minsize(width=300, height=150)
window.config(padx=25, pady=25)

input_box = Entry(width=15)
input_box.get()
input_box.grid(column=1, row=0)

miles_label = Label(text="Mile", font=FONT)
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to", font=FONT)
is_equal_to_label.grid(column=0, row=1)

km_result_label = Label(text=0, font=FONT)
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)


def miles_to_km():
    new_text = round(float(input_box.get()) * 1.609)
    km_result_label.config(text=f"{new_text}")


button1 = Button(text="Calculate", command=miles_to_km)
button1.grid(column=1, row=2)

window.mainloop()
