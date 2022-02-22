from asyncore import write
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    #Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # nr_letters = random.randint(8, 10)
    # nr_symbols = random.randint(2, 4)
    # nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += ([random.choice(letters) for _ in range(random.randint(8, 10))])
    password_list += ([random.choice(symbols) for _ in range(random.randint(2, 4))])
    password_list += ([random.choice(numbers) for _ in range(random.randint(2, 4))])

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char

    # print(f"Your password is: {password}")
    password_input.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    if len(website) == 0 or len(password) == 0:
        is_ok = False
        messagebox.showwarning(title="Ooops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are teh details entered: \nEmail:{username} \nPassword:{password} \nIs it ok to save?")
    if is_ok:
        with open(".\\29\\password.txt", mode='a') as data:
            output = f"{website} | {username} | {password}\n"
            data.write(output)
            website_input.delete(0,END)
            password_input.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=55, pady=55)
canvas = Canvas(width=200,height=200)
lock_img = PhotoImage(file=".//29//logo.png")
canvas.create_image(100,100, image=lock_img)
canvas.grid(row=0,column=0,columnspan=3)

# Website input
website_label = Label(text="Website:",font=("Ariel", 10))
website_label.grid(row=1,column=0)
website_input = Entry(width=35)
website_input.focus()
website_input.grid(row=1,column=1,columnspan=2)

# Username input
username_label = Label(text="Email/Username:",font=("Ariel", 10))
username_label.grid(row=2,column=0)
username_input = Entry(width=35)
username_input.insert(0,"russ@johnsonville.net")
username_input.grid(row=2,column=1,columnspan=2)

# Password input
password_label = Label(text="Password:",font=("Ariel", 10))
password_label.grid(row=3,column=0)
password_input = Entry(width=17)
password_input.grid(row=3,column=1)
password_generate_button = Button(text="Generate Password", command=generate_password)
password_generate_button.grid(row=3,column=2)

# Add button
add_password_button = Button(text="Add", width=30, command=save_password)
add_password_button.grid(row=4,column=1,columnspan=2)

mainloop()