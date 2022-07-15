from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=["POST"])
def receive_data():
    return '<h1>Name: {}, Password: {}</h1>'.format(request.form['name'],request.form["password"])

if __name__ == "__main__":
    app.run(debug=True)