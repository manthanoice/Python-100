from tkinter import *
from tkinter import messagebox
import random
import pyperclip
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

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title='Empty Detail', message='One of the detail is empty, please recheck')
    else:
        is_ok = messagebox.askokcancel(title=website, message='''These are the details you've entered: \n\nEmail: {}\nPassword: {}\n\nIs it OK to save?'''.format(email, password))
        if is_ok:
            with open('the_dataaa.txt', mode='a') as file:
                file.write("{} | {} | {}\n".format(website, email, password))
                website_entry.delete(0, END)
                password_entry.delete(0, END)

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
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

#email
email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'mvbosamiya20@gmail.com')

#password label and button
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)
password_entry = Entry(width=17)
password_entry.grid(row=3, column=1)

password_button = Button(text='Generate Password', width=14, command=gen_password)
password_button.grid(row=3, column=2)

#add button
add_button = Button(text='Add', width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()