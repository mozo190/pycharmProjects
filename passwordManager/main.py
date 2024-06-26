import json
import random
from tkinter import *
from tkinter import messagebox

import pyperclip


# Password Generator Project
# ------------------------------------ SEARCH ----------------------------------- #
def search():
    website = website_input.get()
    try:
        with open("pass.json", "r") as search_data:
            data = json.load(search_data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file yet")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="Result", message=f"Search result: \n Email: {email}\n Password: {password} ")
        else:
            messagebox.showerror(title="Error", message=f"Error, no such {website} saved")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if website == "" or password == "":
        messagebox.showerror(title="Something wrong", message="Please don't leave any fields empty!")
    else:
        try:
            with open("pass.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("pass.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        else:
            # Updating old data with new data
            data.update(new_data)

            with open("pass.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
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

website_input = Entry(width=37)
website_input.grid(column=1, row=1)
website_input.focus()

website_search = Button(text="Search", width=10, command=search)
website_search.grid(column=2, row=1)

email_label = Label(text="Email/Username: ", font=("Arial", 10, "normal"))
email_label.grid(column=0, row=2)

email_input = Entry(width=50)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "pelda@gmail.com")

password_label = Label(text="Password: ", font=("Arial", 10, "normal"))
password_label.grid(column=0, row=3)

password_input = Entry(width=37)
password_input.grid(column=1, row=3)

generate_password_button = Button(text="Gen. Passw", width=10, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
