from tkinter import *
from tkinter import messagebox
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
from random import choice, randint,shuffle
def search():
    website = website_entry.get()
    user = username_box.get()
    password = password_box.get()

def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(0, nr_letters)]
    password_symbol = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]
    password_list = password_numbers + password_symbol + password_letters

    shuffle(password_list)

    password = "".join(password_list)
    password_box.insert(0,password)

    pyperclip.copy(password)

#---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    name_of_website = website_box.get()
    name_of_user = username_box.get()
    password = password_box.get()

    if len(password) == 0 or len(name_of_website) == 0:
        messagebox.showinfo(title="ERROR",message="Please make sure you have filled every entry.");
    else:
            else:
        try:
           with open("data.json", "w") as data_file:
               data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #updating the old data with new data.
            data.update(new_data)
            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_box.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")


logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=300, height=300, highlightthickness=0)
canvas.create_image(200, 189, image=logo_img)


website_box = Entry(width=36)
website_name = Label(text="Website:", width=36,)
username_name = Label(text="Email/Username:", width=36)
username_box = Entry(width=36)
password_name =Label(text="Password:", width=36)
password_box = Entry(width=36)
generate_password = Button(text="Generate Password", width=18,command=generate)
add = Button(text="Add", width=18, command=save)
username_box.insert(0, "kavi@email.com")
search = Button(text="Search",width=18,)


canvas.grid(row=0, column=1)
password_name.grid(row=3, column=0)
username_name.grid(row=2, column=0)
website_name.grid(row=1, column=0)
website_box.focus()
username_box.grid(row=2, columnspan=2,column=1)
generate_password.grid(row=3, column=2)
add.grid(row=4, column=0, columnspan=3)
password_box.grid(row=3, column=1, columnspan=2)
website_box.grid(row=1, column=1, columnspan=2)
search.grid(row=1,column=3)

window.mainloop()
