from flask import Flask, request
from flask import render_template
import requests
import smtplib
from email.mime.text import MIMEText
import creds

app = Flask(__name__)

YAHOO_ACCOUNT=creds.my_email
YAHOO_PASS=creds.password

def send_mail(fromAddr, toAddrs, subject, body):
    msg = MIMEText(body)
    msg['From'] = fromAddr
    msg['To'] = toAddrs
    msg['Subject'] = subject
    with smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465) as connection:
        connection.ehlo()
        connection.login(YAHOO_ACCOUNT, YAHOO_PASS)
        connection.sendmail(fromAddr, toAddrs, msg.as_string())


@app.route('/')
def main_page():
    posts_url = "https://api.npoint.io/abdffc93f5fa1e1e2623"
    posts = requests.get(posts_url).json()
    return render_template('index.html', posts=posts)

@app.route('/about')
def get_about():
    return render_template('about.html')

@app.route('/contact', methods=["GET","POST"])
def get_contact():
    if request.method == 'POST':
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        body_text = f"Name: {data['name']} \nEmail: {data['email']} \nPhone: {data['phone']} \nMessage: {data['message']} \n"
        send_mail(creds.my_email, creds.pers_email, "Contact form submition", body_text)
        return render_template('contact.html', contact_title = 'Successfully sent your message')
    else:
        return render_template('contact.html', contact_title = 'Contact Me')

@app.route('/post/<blog_id>')
def get_post(blog_id):
    return_post = {}
    posts_url = "https://api.npoint.io/abdffc93f5fa1e1e2623"
    posts = requests.get(posts_url).json()
    for post in posts:
        if post['id'] == int(blog_id):
            print(post)
            return_post = post
    return render_template("post.html",post=return_post) 

@app.route('/form-entry', methods=["POST"])
def receive_data():
    data = request.form
    print(data["name"])
    print(data["email"])
    print(data["phone"])
    print(data["message"])
    return '<h1>Successfully sent your message</h1>'

if __name__ == "__main__":
    app.run(debug=True)
