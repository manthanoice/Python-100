from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

#Reading into csv file
df = pd.read_csv(r'E:\Python 100\Day-31\data\french_words.csv')
learning_data = df.to_dict(orient='records')
# back_image = PhotoImage(file='Day-31\images\card_back.png')
current_card = {}

#Defining Functions
def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(learning_data)
    canvas.itemconfig(card_title, text = 'French', fill = 'black')
    canvas.itemconfig(card_word, text = current_card['French'], fill = 'black')
    canvas.itemconfig(card_image, image = card_front_image)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_image, image=card_back_image)

#Creating window
window = Tk()
window.title('Flashyyy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

#Creating Canvas
canvas = Canvas(width=800, height=526)
card_back_image = PhotoImage(file='Day-31\images\card_back.png')
card_front_image = PhotoImage(file='Day-31\images\card_front.png')
card_image = canvas.create_image(400, 263, image = card_front_image)
card_title = canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic', 'underline'))
card_word = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

#buttons and images
correct_image = PhotoImage(file=r'Day-31\images\right.png')
correct_button = Button(image=correct_image, highlightthickness=0, command=next_card)
correct_button.grid(row=1, column=0)

wrong_image = PhotoImage(file=r'Day-31\images\wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=1)

next_card()

window.mainloop()