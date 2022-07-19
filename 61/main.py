from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators

app = Flask(__name__)
app.secret_key = "iIS3gE33R6U4Rt52"

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[validators.DataRequired(),validators.Email()])
    password = PasswordField(label='Password', validators=[validators.DataRequired(), validators.length(min=8)])
    submit = SubmitField(label='Login')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm(request.form)
    print(form.validate_on_submit())
    if request.method == 'POST' and form.validate_on_submit():
        return render_template('success.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)