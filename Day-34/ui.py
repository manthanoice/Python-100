from tkinter import *
from quiz_brain import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        #windows
        self.windows = Tk()
        self.windows.title(string='Sizzlers bitches')
        self.windows.config(bg=THEME_COLOR, padx=20, pady=20)

        #photoimage for true and false
        self.true = PhotoImage(file=r'Day-34\images\true.png')
        self.false = PhotoImage(file=r'Day-34\images\false.png')

        #label
        self.score_label = Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        #canvas
        self.canvas = Canvas(height=250, width=300, bg='white')
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text='Some question', 
            fill=THEME_COLOR, 
            font=('Arial', 16, 'italic')
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        #buttons using image
        self.true_button = Button(image = self.true, highlightthickness=0)
        self.false_button = Button(image = self.false, highlightthickness=0)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.the_next_question()
        #ending
        self.windows.mainloop()
    
    def the_next_question(self):
        the_question_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text = the_question_text)