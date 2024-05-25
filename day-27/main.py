import tkinter

window = tkinter.Tk()
window.title("This is my first GUI program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.place(x=0, y=200)

my_label["text"] = "New text"


# my_label.config(text="newer text")
def button_clicked():
    # print("I got clicked")
    new_text = input_.get()
    my_label.config(text=new_text)
    # my_label["text"] = input_


# button
button = tkinter.Button(text="click me", command=button_clicked)
button.pack()

# Entry
input_ = tkinter.Entry(width=10)
input_.pack()
print(input_.get())

window.mainloop()
