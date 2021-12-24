from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for i in range(random.randint(6, 8))]
    password_symbols = [random.choice(symbols) for i in range(random.randint(2, 4))]
    password_numeber = [random.choice(numbers) for i in range(random.randint(2, 4))]

    final_password = password_letters + password_symbols + password_numeber
    random.shuffle(final_password)

    password = "".join(final_password)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    json_dict = {
        website: {
            'email': email,
            'password': password
        }
    }

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title='Empty Detail', message='One of the detail is empty, please recheck')
    else:
        try:
            with open('data.json', mode='r') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            with open('data.json', mode='w') as json_file:
                json.dump(json_dict, json_file, indent=4)
        else:
            if website in data and email in data[website]['email']:
                messagebox.showerror(title='Error', message='The entry already exists')
            else:
                data.update(json_dict)
                with open('data.json', mode='w') as json_file:
                    json.dump(data, json_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- Finding Password ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open('data.json') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No data found')
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message='For {} your,\nEmail: {}\nPassword: {}'.format(website, email, password))
        else:
            messagebox.showerror(title=website, message='You have not added any email and password yet for {}, please try searching again after entering the details'.format(website))

# ---------------------------- UI SETUP ------------------------------- #

#The window
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

#The canvas
canvas = Canvas(width=200, height=200)
pass_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=pass_image)
canvas.grid(row=0, column=1)

#website
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

#email
email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)
email_entry = Entry(width=39)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'mvbosamiya20@gmail.com')

#password label and button
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

password_button = Button(text='Generate Password', width=14, command=gen_password)
password_button.grid(row=3, column=2)

#add button
add_button = Button(text='Add', width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)

#search buttton
search_button = Button(text='Search', width=13, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()