from tkinter import *
import requests

#Fucntion that will get  request from API and change text in canvas
def get_quote():
    kanye = requests.get(url='https://api.kanye.rest/')
    kanye_text = kanye.json()
    kanye_quote = kanye_text['quote']
    canvas.itemconfig(quote_text, text = kanye_quote)

#Creating windows
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

#Creating Canvas
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=r'Day-33\background.png')
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Click Kanye for his quotes", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

#Creating Kanye image or should I say 'Ye'
kanye_img = PhotoImage(file="Day-33\kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

#Loop
window.mainloop()