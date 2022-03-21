from time import sleep
from tkinter import *
from turtle import bgcolor
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # Score label
        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        # Question Canvas
        self.question_canvas = Canvas(height=250, width=300, background="white",highlightthickness=0)
        self.question_canvas_text = self.question_canvas.create_text(150, 125, text="Question here", font=("Arial",20,"italic"), fill=THEME_COLOR, width=280)
        self.question_canvas.grid(column=0,row=1, columnspan=2, pady=50)

        # Buttons
        true_button_img = PhotoImage(file=".\\34\\images\\true.png")
        self.true_button = Button(image=true_button_img, activebackground=THEME_COLOR, highlightthickness=0, command=self.click_true)
        self.true_button.grid(column=0, row=2)

        false_button_img = PhotoImage(file=".\\34\\images\\false.png")
        self.false_button = Button(image=false_button_img, activebackground=THEME_COLOR, highlightthickness=0, command=self.click_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_canvas.config(background="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_canvas_text, text=q_text)
        else:
            self.question_canvas.itemconfig(self.question_canvas_text, text="You have reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    
    def click_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)
    
    def click_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)
    
    def give_feedback(self, is_correct):
        if is_correct:
            self.question_canvas.config(bg="green")
        else:
            self.question_canvas.config(bg="red")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000, self.get_next_question)    

        