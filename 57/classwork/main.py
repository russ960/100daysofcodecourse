from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    copyright_year = datetime.today().year
    return render_template("index.html", year=copyright_year)

@app.route('/guess/<name>')
def guess_gender_age(name):
    name = name.title()
    agify_url = f"https://api.agify.io?name={name}"
    age = requests.get(agify_url).json()["age"]

    genderize_url = f"https://api.genderize.io?name={name}"
    gender = requests.get(genderize_url).json()["gender"]
    
    return render_template("index_age_gender.html", entered_name=name, agify=age, genderize=gender)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)
    
if __name__ == "__main__":
    app.run(debug=True)


