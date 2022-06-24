from flask import Flask
from random import randint
app = Flask(__name__)

@app.route("/")
def welcome():
    return '<h1> Guess a number between 0 and 9 </h1><br> <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

rand_number = randint(0,9)

@app.route("/<int:number>")
def higher_lower(number):
    if rand_number < number:
        return_code = '<h1 style="color:Purple"> Too high, try again! </h1> <br> <img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    if rand_number > number:
        return_code = '<h1 style="color:Red"> Too low, try again! </h1> <br> <img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    if rand_number == number:
        return_code = '<h1 style="color:Green"> You found me! </h1> <br> <img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    return f'{return_code}'


print(__name__)
if __name__ == "__main__":
    app.run(debug=True)
