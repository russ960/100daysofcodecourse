from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    posts_url = "https://api.npoint.io/c790b4d5cab58020d391"
    posts = requests.get(posts_url).json()
    return render_template("index.html",posts=posts)

@app.route('/post/<blog_id>')
def get_post(blog_id):
    return_post = {}
    posts_url = "https://api.npoint.io/c790b4d5cab58020d391"
    posts = requests.get(posts_url).json()
    for post in posts:
        if post['id'] == int(blog_id):
            print(post)
            return_post = post
    return render_template("post.html",post=return_post)

if __name__ == "__main__":
    app.run(debug=True)
