from tkinter import *
from tkinter import font
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
check_mark = ''
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global check_mark
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    title_label.config(text='Timer',fg=GREEN)
    check_mark = ''
    check_mark_label.config(text=check_mark)
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        title_label.config(text='Work', fg=GREEN)
        count_down(work_secs)
    elif reps % 8 == 0:
        title_label.config(text='Break', fg=RED)
        count_down(long_break_secs)
    else:
        title_label.config(text='Break', fg=PINK)
        count_down(short_break_secs)

    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global check_mark
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        if reps % 2 == 0:
            check_mark += "✔"
            check_mark_label.config(text=check_mark)
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=".//28//tomato.png")

def say_something(thing):
    print(thing)


title_label = Label(text='Timer', font=(FONT_NAME,35,"bold"), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)

canvas.create_image(100,112,image=tomato_img)
canvas.grid(column=1, row=0)
timer_text = canvas.create_text(100,130,text='00:00',fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1, row=1)


start_button = Button(text='Start', command=start_timer)
start_button.grid(column=0, row=2)

stop_button = Button(text='Reset', command=reset_timer)
stop_button.grid(column=2, row=2)


check_mark_label = Label(bg=YELLOW, fg=GREEN)
check_mark_label.grid(column=1, row=3)



window.mainloop()