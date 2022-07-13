from flask import Flask, send_from_directory
from flask import render_template
import requests

app = Flask(__name__)



@app.route('/')
def main_page():
    posts_url = "https://www.npoint.io/docs/abdffc93f5fa1e1e2623"
    posts = requests.get(posts_url).json()
    return render_template('index.html', posts=posts)

@app.route('/about')
def get_about():
    return render_template('about.html')

@app.route('/contact')
def get_contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
