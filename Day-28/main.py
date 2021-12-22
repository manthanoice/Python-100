from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        counter(long_break_sec)
        title_label.config(text='Break', fg=RED)
    if reps % 2 == 0:
        counter(short_break_sec)
        title_label.config(text='Breka', fg=PINK)
    else:
        counter(work_sec)
        title_label.config(text='Break', fg=GREEN)
         
    counter(10)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def counter(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    canvas.itemconfig(timer, text="0{}:{}".format(count_min, count_sec))
    if count>0:
        window.after(1000, counter, count-1)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=60, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
title_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer = canvas.create_text(100, 134, text='00:00', fill='white', font=(FONT_NAME, 30, 'bold'))
start = Button(text='Start', highlightthickness=0, command=start_timer)
stop = Button(text='Stop', highlightthickness=0)
check_mark = Label(text='✔️', bg=YELLOW)
title_label.grid(row=0, column=1)
canvas.grid(row= 1,column= 1)
start.grid(row= 2,column= 0)
stop.grid(row= 2,column= 2)
check_mark.grid(row=3, column=1)

window.mainloop()