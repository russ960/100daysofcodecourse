from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'jkl;dfasoi7kljfoier'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()


@app.route('/')
def home():
    print(current_user.is_authenticated)
    return render_template("index.html")

@app.route('/download')
@login_required
def download():
    filename = 'files/cheat_sheet.pdf'
    return send_from_directory('static',filename)

@app.route('/register', methods=["GET","POST"])
def register():
    if request.method == 'POST':
        hashed_password = generate_password_hash(request.form["password"], method='pbkdf2:sha256', salt_length=8)
        email = User.query.filter_by(email=request.form["email"]).first()
        if email:
            flash("That email already exists, login instead.")
            return render_template('login.html')
        else:
            new_user = User(
                email = request.form["email"],
                password = hashed_password,
                name = request.form["name"]
            )
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("secrets", name=new_user.name))
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('secrets', name=user.name))
            else:
                flash("Incorrect password entered, please try again.")
                return render_template('login.html')
        else:
            flash("That email does not exist, please try again.")
            return render_template('login.html')
        
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    name = request.args.get('name')
    return render_template("secrets.html", name=name)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
