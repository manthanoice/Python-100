from tkinter import *

window = Tk()
window.title('Hehe')
window.minsize(height=600, width=600)
my_label = Label(text='Hehe part 2', font=('Comic Sans MS', 40, 'italic'))
my_label.pack()
def text_listener():
    my_label.config(text='Hehe you clicked the button')

entry = Entry(width=30)
entry.insert(END, string='Hehehehehehhehehehe')
entry.pack()
entry.get()

text = Text(height=5, width=30)
text.focus()
text.pack()

def spineer_listen():
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=14, width=5, command=spineer_listen)
spinbox.pack()

def button_listener():
    my_label.config(text=entry.get())

button = Button(text='Hello', command=button_listener)
button.pack()



window.mainloop()