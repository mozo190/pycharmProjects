import tkinter

window = tkinter.Tk()
window.title("This is my first GUI program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a label", font=("Arial", 14, "bold"))
# my_label.place(x=0, y=200)
my_label.grid(column=0, row=0)

my_label["text"] = "New text"


# my_label.config(text="newer text")
def button_clicked():
    # print("I got clicked")
    new_text = input_.get()
    my_label.config(text=new_text)
    # my_label["text"] = input_


# button
button = tkinter.Button(text="click me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = tkinter.Button(text="Button")
new_button.grid(column=2, row=0)

# Entry
input_ = tkinter.Entry(width=10)
input_.get()
input_.grid(column=3, row=2)

window.mainloop()
