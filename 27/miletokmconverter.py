from tkinter import *
from turtle import width

def mile_to_km():
    km = float(input.get()) * 1.609344
    result_label.config(text=km)

window = Tk()
#window.minsize(200,100)
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# miles numerical box
input = Entry(width=7)
input.grid(row=0,column=1)

# miles label
miles_label = Label(text="Miles")
miles_label.grid(row=0,column=2)

# equal label
equalto_label = Label(text="is equal to")
equalto_label.grid(row=1,column=0)

# result label
result_label = Label(text="0")
result_label.grid(row=1,column=1)

# km label
km_label = Label(text="Km")
km_label.grid(row=1,column=2)

# calculate button
calculate_button = Button(text="Calculate", command=mile_to_km)
calculate_button.grid(row=2,column=1)

window.mainloop()