from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
import creds

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)

class Update_Form(FlaskForm):
    rating = FloatField('Your rating out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField('Your review', validators=[DataRequired()])
    submit = SubmitField('Submit')

class Add_Form(FlaskForm):
    movie_name = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.String(4), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    rating = db.Column(db.Float(), nullable=False)
    ranking = db.Column(db.Integer(), nullable=False)
    review = db.Column(db.Text(), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

db.create_all()

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()

# @app.route('/', defaults={'id':1})
# @app.route("/<string:id>", methods=['GET','POST'])
# def home(id: int):  
@app.route('/')
def home():
    # movie_details = Movie.query.filter_by(id=id).first()
    movie_details = Movie.query.order_by(Movie.rating).all()

    for id in range(len(movie_details)):
        movie_details[id].ranking = len(movie_details) - id
    db.session.commit()
    return render_template("index.html", movie_details=movie_details)

@app.route('/update', methods=['GET','POST'])
def update():
    form = Update_Form()
    id=request.args.get('id')
    data = request.form
    if form.validate_on_submit():
        movie_details = Movie.query.filter_by(id=id).first()
        movie_details.rating = float(data["rating"])
        movie_details.review =  data["review"]
        db.session.commit()
        id = None
        return redirect(url_for('home'))
    return render_template("edit.html", form=form)

@app.route('/delete')
def delete_movie():
    id=request.args.get('id')
    Movie.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/add', methods=['GET','POST'])
def add_movie():
    form = Add_Form()
    data = request.form
    if form.validate_on_submit():
        payload = {"api_key":creds.tmdb_api, 'language':'en-US', 'query':data["movie_name"], 'page':1, 'include_adult':'false'}
        response = requests.get('https://api.themoviedb.org/3/search/movie', params=payload).json()["results"]
        return render_template("select.html", json_output=response)
    return render_template("add.html", form=form) 

@app.route('/select', methods=['GET','POST'])
def select_move(json_output):
    print(json_output)

@app.route('/insert')
def insert_movie():
    movie_id=request.args.get('id')
    payload = {"api_key":creds.tmdb_api, 'language':'en-US'}
    movie_json = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}', params=payload).json()
    title = movie_json["original_title"]
    year = movie_json["release_date"]
    description = movie_json["overview"]
    rating = movie_json["vote_average"]
    img_url = f'https://image.tmdb.org/t/p/w500{movie_json["poster_path"]}'
    new_movie = Movie(
        title=title,
        year=year[0:4],
        description=description,
        rating=rating,
        ranking=10,
        review="",
        img_url=img_url
    )
    db.session.add(new_movie)
    db.session.flush()
    inserted_id = new_movie.id
    db.session.commit()

    return redirect(url_for('update', id=inserted_id))
    

if __name__ == '__main__':
    app.run(debug=True)
