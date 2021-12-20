from tkinter import *

#Defining function that will return the miles answer
def miles_to_the_km(miles):
    return round(float(miles)*1.6)

#Defining function that will replace text in the label
def the_label_changer():
    new_text = the_input.get()
    answer.config(text=(miles_to_the_km(new_text)))

#Creating windows
windows = Tk()
windows.config(padx=20, pady=20)

#Creating entry for user input
the_input = Entry()
the_input.grid(row=1, column=0)

#Creating label
miles_label = Label(text='Miles')
miles_label.grid(row=2, column=0)

#Creating label
equal_to_label = Label(text='is equal to')
equal_to_label.grid(row=0, column=1)

#Creating label
answer = Label(text='0')
answer.grid(row=1, column=1)

#Creating label
the_km_label = Label(text='Km')
the_km_label.grid(row=2, column=1)

#Creating button
button = Button(text='Calculate', command=the_label_changer)
button.grid(row=1, column=2)

#Closing the windows
windows.mainloop()