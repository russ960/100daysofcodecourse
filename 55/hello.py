from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def bold_wrapper():
        return f"<b>{function()}</b>"
    return bold_wrapper

def make_underlined(function):
    def underlined_wrapper():
        return f"<u>{function()}</u>"
    return underlined_wrapper

def make_emphasis(function):
    def emphasis_wrapper():
        return f"<em>{function()}</em>"
    return emphasis_wrapper

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, your are {number} years old!"

print(__name__)

if __name__ == "__main__":
    app.run(debug=True)