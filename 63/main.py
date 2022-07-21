from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# db = sqlite3.connect("63/books-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

db.create_all()

def __repr__(self):
    return f'<Book {self.title}>'

all_books = []

@app.route('/')
def home():
    all_books = Books.query.all()
    return render_template('index.html', all_books=all_books)


@app.route("/add", methods=['GET','POST'])
def add():
    if request.method == 'POST':
        new_book = Books(title=request.form["book_name"], author=request.form["author_name"], rating=float(request.form["rating"]))
        db.session.add(new_book)
        db.session.commit()

        output_dict = {}
        output_dict["book_name"] = request.form["book_name"]
        output_dict["author_name"] = request.form["author_name"]
        output_dict["rating"] = request.form["rating"]
        all_books.append(output_dict)
    return render_template('add.html')

@app.route("/edit", methods=['GET','POST'])
def edit():
    id=request.args.get('id')
    if request.method == 'POST':
        data = request.form 
        book_details = Books.query.filter_by(id=id).first()
        book_details.rating = float(data["new_rating"])
        db.session.commit()
        return redirect(url_for('home'))
    else:
        book_details = Books.query.filter_by(id=id).first()
        return render_template('edit.html', book=book_details)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

