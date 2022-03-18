from tkinter import *
from turtle import bgcolor

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.current_score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # Score label
        self.score_label = Label(text=f"Score: {self.current_score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        # Question Canvas
        self.question_canvas = Canvas(height=250, width=300, background="white",highlightthickness=0)
        self.question_canvas_text = self.question_canvas.create_text(150, 125, text="Question here", font=("Arial",20,"italic"), fill=THEME_COLOR)
        self.question_canvas.grid(column=0,row=1, columnspan=2, pady=50)

        # Buttons
        true_button_img = PhotoImage(file=".\\34\\images\\true.png")
        self.true_button = Button(image=true_button_img, activebackground=THEME_COLOR, highlightthickness=0)
        self.true_button.grid(column=0, row=2)

        false_button_img = PhotoImage(file=".\\34\\images\\false.png")
        self.false_button = Button(image=false_button_img, activebackground=THEME_COLOR, highlightthickness=0)
        self.false_button.grid(column=1, row=2)



        self.window.mainloop()
