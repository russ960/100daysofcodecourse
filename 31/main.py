from cgitb import text
from email.mime import image
from tkinter import *
import pandas as pd
from random import choice
import os

current_language = "French"
current_word = {}
BACKGROUND_COLOR = "#B1DDC6"
words_to_learn_file = ".//31//data//words_to_learn.csv"
source_words_file = ".//31//data//french_words.csv"

# Data Ingestion
csv_location = ''
if os.path.exists(words_to_learn_file):
    csv_location = words_to_learn_file
else:
    csv_location = source_words_file
df = pd.read_csv(csv_location)
data_dict = df.to_dict(orient="records")

# New Word Function
def new_word():
    global current_language, current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = choice(data_dict)
    current_language = 'French'
    canvas.itemconfig(background_image, image=front_img)
    canvas.itemconfig(tanslated_word, text=current_word[current_language], fill='black')
    canvas.itemconfig(language, text=current_language, fill='black')
    flip_timer = window.after(3000, flip)


def flip():
    global current_language
    current_language = 'English'
    canvas.itemconfig(background_image, image=back_img)
    canvas.itemconfig(tanslated_word, text=current_word[current_language], fill='white')
    canvas.itemconfig(language, text=current_language, fill='white')

def known_word():
    global current_word, data_dict, words_to_learn_file
    data_dict.remove(current_word)
    df_out = pd.DataFrame(data_dict)
    df_out.to_csv(words_to_learn_file, index=False)
    new_word()

# UI Configuration
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip)

canvas = Canvas(width=850,height=576, bg=BACKGROUND_COLOR, highlightthickness=0)
back_img = PhotoImage(file=".//31//images//card_back.png")
front_img = PhotoImage(file=".//31//images//card_front.png")
background_image = canvas.create_image(425,263, image=front_img)
language = canvas.create_text(400,150, text="French", font=("Ariel", 40, "italic"))
tanslated_word = canvas.create_text(400,263, text="trouve", font=("Ariel", 60, "bold"))
canvas.grid(row=0,column=0, columnspan=2)

wrong_button_image = PhotoImage(file=".\\31\\images\\wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=new_word)
wrong_button.grid(row=1,column=0)

correct_button_image = PhotoImage(file=".\\31\\images\\right.png")
correct_button = Button(image=correct_button_image, highlightthickness=0, command=known_word)
correct_button.grid(row=1,column=1)
new_word()


mainloop()