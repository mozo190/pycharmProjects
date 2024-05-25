from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {email}"
                           f"\nPassword: {password} \nIs it ok to save?")

    with open("pass.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")
        website_input.delete(0, END)
        password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=5, highlightcolor="black")
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ", font=("Arial", 10, "normal"))
website_label.grid(column=0, row=1)

website_input = Entry(width=50)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_label = Label(text="Email/Username: ", font=("Arial", 10, "normal"))
email_label.grid(column=0, row=2)

email_input = Entry(width=50)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "pelda@gmail.com")

password_label = Label(text="Password: ", font=("Arial", 10, "normal"))
password_label.grid(column=0, row=3)

password_input = Entry(width=37)
password_input.grid(column=1, row=3)

generate_password_button = Button(text="Gen. Passw", width=10)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
