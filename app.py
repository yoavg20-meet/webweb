from databases import *
from flask import Flask, request, redirect, render_template, url_for
from flask import session as login_session
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yoyo20meet@gmail.com' #fll in
app.config['MAIL_PASSWORD'] = 'meetyear20' #fill in
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def home(): 
    return render_template('donation.html')
    

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        user = get_user(request.form['username'])
        if user != None and user.verify_password(request.form["password"]):
            login_session['name'] = user.username
            login_session['logged_in'] = True
            return logged_in()
        else:
            return redirect(url_for('signup'))
    return render_template('login.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == "GET":
        return render_template('signup.html')
        
    else:
        #check that username isn't already taken
        user = get_user(request.form['username'])
        if user == None:
            add_user(request.form['username'],request.form['password'])
        return home()


@app.route('/logged-in')
def logged_in():
    return render_template('logged.html')


@app.route('/logout')
def logout():
    return home()

@app.route('/email' , methods=['GET' ,'POST'])
def email():
    if request.method == 'GET':
        return render_template('donation.html')
    else:    
        msg = Message('Hello', sender = 'yoyo20meet@gmail.com', recipients = ['ron12harel@gmail.com'])
        msg.body = request.form['message'] +"\n"+request.form["email"]
        mail.send(msg)
        return "Sent"
    



if __name__ == '__main__':
    app.run(debug=True)