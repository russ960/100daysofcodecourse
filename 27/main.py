import tkinter

def button_clicked():
    my_label.config(text=input.get())

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(500,300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text='I am a label', font=("Ariel", 24, "bold"))
my_label.grid(column=0, row=0)

# button 1
my_button = tkinter.Button(text="Click Me", command=button_clicked)
my_button.grid(column=1, row=1)

# button 2
my_other_button = tkinter.Button(text="Click Me Too")
my_other_button.grid(column=2, row=0)

# input
input = tkinter.Entry()
input.grid(column=3, row=2)

window.mainloop()