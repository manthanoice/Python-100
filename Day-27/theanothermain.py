from tkinter import *

def button_clicked():
    print('Clicked me Daddy')
    new_text = the_input.get()
    my_label.config(text=new_text)

#windows
windows = Tk()
windows.title('Urusai')
windows.minsize(height=300, width=300)
windows.config(padx=200, pady=100)

#Label
my_label = Label(text='Surprise mfs', font=('Arial', 24, 'bold'))
my_label.grid(row=0, column=0)

#Button
button = Button(text='Click me Daddy', command = button_clicked)
button.grid(row=1, column=1)

#New Button
new_button = Button(text='New button')
new_button.grid(row=0, column=2)

#Entry
the_input = Entry()
the_input.grid(row=3, column=3)

#Ending the program
windows.mainloop()