from tkinter import *
from tkinter import messagebox
from random import randint
import random
from pyperclip import copy
import json

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_fun():
    password_string = [random.choice(LETTERS) for i in range(randint(2, 4))]
    password_string += [random.choice(NUMBERS) for i in range(randint(2, 4))]
    password_string += [random.choice(SYMBOLS) for i in range(randint(2, 4))]
    random.shuffle(password_string)
    new_password = "".join(password_string)
    copy(new_password)
    # password_entry.delete(0,"end")
    password_entry.insert(0, new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    field1 = website_entry.get()
    field2 = email_entry.get()
    field3 = password_entry.get()
    new_data = {
        field1: {
            "email": field2,
            "password": field3
        }
    }
    # print(len(field3))
    if len(field1) == 0 or len(field3) == 0:
        messagebox.showinfo(title="OOPS", message="Fill all the details\nCheck your details!")
    else:
        try:
            # if_ok = messagebox.askokcancel(title=field1,message=f"Details:\nWebsite: {field1}\nEmail: {
            # field2}\nPassword:{field3}\nDo you want to continue?") if if_ok:
            # data.write(f"{field1} | {field2} | {field3}\n")
            '''Reading from Json file and type check is dict'''
            # print(json.load(data))
            '''Writing data into Json file'''
            # json.dump(new_data, data, indent=4)
            '''Update data into Json file'''

            with open("data.json", mode="r") as data:
                json_data = json.load(data)

        except FileNotFoundError:
            with open("data.json", "w") as data:
                json.dump(new_data, data, indent=4)

        else:
            json_data.update(new_data)
            with open("data.json", "w") as data:
                json.dump(json_data, data, indent=4)

        finally:
            website_entry.delete(0, "end")
            # email_entry.delete(0, "end")
            password_entry.delete(0, "end")


# -------------------------------- SEARCH JSON FILE ---------------------#
def search_func():
    field1 = website_entry.get()
    try:
        with open("data.json", mode="r") as data:
            contents = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title=field1, message="No data found!🙁")
    else:
        if field1 in contents:
            messagebox.showinfo(title=field1,
                                message=f"Email:{contents[field1]['email']}\nPassword:{contents[field1]['password']}")
        else:
            messagebox.showerror(title=field1,message=f"{field1} not found‼️")


# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
# window.minsize(width=400,height=400)
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200 )
lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock)
# canvas.create_text(100, 130, text="Lock image", font=("Arial", 22, "bold"))
canvas.grid(column=1, row=0)

# Labels and Entry
website = Label(text="Website:", font=("Arial", 14))
website.grid(column=0, row=1)

website_entry = Entry(width=30)
website_entry.grid(column=1, row=1, columnspan=1)
website_entry.focus()

email = Label(text="Email/Username:", font=("Arial", 14))
email.grid(column=0, row=2)

email_entry = Entry(width=30)
email_entry.grid(column=1, row=2, columnspan=1)
email_entry.insert(0, "hitesh@gmail.com")

password = Label(text="Password:", font=("Arial", 14))
password.grid(column=0, row=3)

password_entry = Entry(width=30)
password_entry.grid(column=1, row=3, columnspan=1)

# Buttons
generate = Button(text="Generate Password", width=15, command=generate_fun)
generate.grid(column=2, row=3)

add = Button(text="Add", width=50, command=save)
add.grid(column=1, row=5, columnspan=2)

# add.config(bg="blue")
search = Button(text="Search", width=15, command=search_func)
search.grid(column=2, row=1)

window.mainloop()
#-------------------------------------------------------------------------------