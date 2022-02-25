from cgitb import text
from tkinter import *
import pandas as pd
from random import choice
current_language = "French"
BACKGROUND_COLOR = "#B1DDC6"

# Data Ingestion
csv_location = ".//31//data//french_words.csv"
df = pd.read_csv(csv_location)
data_dict = df.to_dict(orient="records")

# New Word Function
def new_word():
    global current_language
    new_word = choice(data_dict)
    canvas.itemconfig(tanslated_word, text=new_word[current_language])
    canvas.itemconfig(language, text=current_language)

# UI Configuration
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=850,height=576, bg=BACKGROUND_COLOR, highlightthickness=0)
back_img = PhotoImage(file=".//31//images//card_back.png")
front_img = PhotoImage(file=".//31//images//card_front.png")
#canvas.create_image(425,263, image=back_img)
canvas.create_image(425,263, image=front_img)
language = canvas.create_text(400,150, text="French", font=("Ariel", 40, "italic"))
tanslated_word = canvas.create_text(400,263, text="trouve", font=("Ariel", 60, "bold"))
canvas.grid(row=0,column=0, columnspan=2)

wrong_button_image = PhotoImage(file=".\\31\\images\\wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=new_word)
wrong_button.grid(row=1,column=0)

correct_button_image = PhotoImage(file=".\\31\\images\\right.png")
correct_button = Button(image=correct_button_image, highlightthickness=0, command=new_word)
correct_button.grid(row=1,column=1)
new_word()

mainloop()